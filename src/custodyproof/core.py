"""File digest and tamper-evident chain, not an accredited forensic process."""
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone

def digest(data):
    return hashlib.sha256(data).hexdigest()

def stable(record):
    return json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()

def read_ledger(path):
    p = Path(path)
    if not p.exists():
        return []
    return [json.loads(line) for line in p.read_text('utf-8').splitlines() if line.strip()]

def verify(path):
    events = read_ledger(path)
    previous = '0' * 64
    for index, event in enumerate(events, 1):
        body = {k: v for k, v in event.items() if k != 'record_hash'}
        if body.get('previous_hash') != previous or digest(stable(body)) != event.get('record_hash'):
            return {'valid': False, 'event': index, 'count': len(events)}
        previous = event['record_hash']
    return {'valid': True, 'count': len(events), 'note': 'Hash chain checks internal integrity, not trusted timestamps or identity.'}

def add(file, ledger, case='DEMO-001', actor='lab'):
    source = Path(file)
    if not source.is_file() or source.is_symlink():
        raise ValueError('Expected a regular local file')
    if source.stat().st_size > 20_000_000:
        raise ValueError('Demo limit is 20 MB per file')
    state = verify(ledger)
    if not state['valid']:
        raise ValueError('Existing ledger integrity invalid; refusing to append')
    events = read_ledger(ledger)
    prev = events[-1]['record_hash'] if events else '0' * 64
    body = {'case': case, 'actor': actor, 'filename': source.name, 'sha256': digest(source.read_bytes()),
            'timestamp_utc': datetime.now(timezone.utc).isoformat(), 'previous_hash': prev, 'event': 'intake'}
    row = dict(body, record_hash=digest(stable(body)))
    with open(ledger, 'a', encoding='utf-8') as out:
        out.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + '\n')
    return {'record': row, 'ledger': str(ledger)}

def configure(sub):
    p=sub.add_parser('add',help='Record SHA-256 of local file')
    p.add_argument('file');p.add_argument('--ledger',default='custody-ledger.jsonl')
    p.add_argument('--case',default='DEMO-001');p.add_argument('--actor',default='lab')
    v=sub.add_parser('verify',help='Check ledger hash chain');v.add_argument('--ledger',default='custody-ledger.jsonl')
    f=sub.add_parser('verify-files',help='Compare stored evidence with ledger digests')
    f.add_argument('--ledger',default='custody-ledger.jsonl');f.add_argument('--directory',required=True)

def run(args):
    if args.command == 'add':
        return add(args.file, args.ledger, args.case, args.actor)
    if args.command == 'verify-files':
        return verify_files(args.ledger, args.directory)
    return verify(args.ledger)

def demo():
    import tempfile
    with tempfile.TemporaryDirectory() as directory:
        source=Path(directory)/'fictional.txt';source.write_text('FAKE DEMONSTRATION CONTENT',encoding='utf-8')
        ledger=Path(directory)/'ledger.jsonl'
        add(source,ledger)
        return verify(ledger)

def verify_files(ledger, directory):
    """Check that currently stored evidence matches recorded SHA-256 hashes.

    This does not establish identity, time of acquisition, or external authenticity.
    """
    state = verify(ledger)
    if not state['valid']:
        return {'valid': False, 'ledger_valid': False, 'checked': 0, 'errors': ['ledger-integrity-invalid']}
    root = Path(directory).resolve(strict=True)
    if not root.is_dir():
        raise ValueError('Evidence directory must be a directory')
    errors = []
    checked = 0
    for i, event in enumerate(read_ledger(ledger), start=1):
        if event.get('event') != 'intake':
            continue
        checked += 1
        name = event.get('filename')
        if not isinstance(name, str) or not name or name in ('.', '..') or Path(name).name != name:
            errors.append({'event': i, 'reason': 'unsafe-filename'})
            continue
        file = root / name
        if file.is_symlink() or not file.is_file():
            errors.append({'event': i, 'reason': 'missing-or-symlink', 'filename': name})
            continue
        hasher = hashlib.sha256()
        with file.open('rb') as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b''):
                hasher.update(block)
        if hasher.hexdigest() != event.get('sha256'):
            errors.append({'event': i, 'reason': 'digest-mismatch', 'filename': name})
    return {'valid': not errors, 'ledger_valid': True, 'checked': checked, 'errors': errors,
            'note': 'Local file comparison only; not proof of provenance or trusted time.'}
