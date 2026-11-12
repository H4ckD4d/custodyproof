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
