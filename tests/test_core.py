import tempfile, unittest, json
from pathlib import Path
from custodyproof.core import add, verify
class CoreTests(unittest.TestCase):
    def test_chain(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); f=p/'demo.txt';f.write_text('fake');ledger=p/'ledger.jsonl'
            add(f,ledger);add(f,ledger)
            self.assertEqual(verify(ledger)['count'],2)
            self.assertTrue(verify(ledger)['valid'])
    def test_tampering_is_detected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); f=p/'demo.txt';f.write_text('fake');ledger=p/'ledger.jsonl'
            add(f,ledger)
            row=json.loads(ledger.read_text().splitlines()[0]);row['actor']='modified';ledger.write_text(json.dumps(row)+'\n')
            self.assertFalse(verify(ledger)['valid'])

    def test_verify_files_matches_and_detects_modified_file(self):
        from custodyproof.core import verify_files
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); f=p/'evidence.txt'; f.write_text('synthetic evidence'); ledger=p/'ledger.jsonl'
            add(f,ledger)
            self.assertTrue(verify_files(ledger,p)['valid'])
            f.write_text('modified evidence')
            result=verify_files(ledger,p)
            self.assertFalse(result['valid'])
            self.assertEqual(result['errors'][0]['reason'], 'digest-mismatch')
    def test_verify_files_rejects_symlink(self):
        from custodyproof.core import verify_files
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); f=p/'evidence.txt'; f.write_text('synthetic evidence'); ledger=p/'ledger.jsonl'
            add(f,ledger)
            f.unlink(); (p/'elsewhere.txt').write_text('synthetic evidence'); f.symlink_to(p/'elsewhere.txt')
            self.assertEqual(verify_files(ledger,p)['errors'][0]['reason'], 'missing-or-symlink')
