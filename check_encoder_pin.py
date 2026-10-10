import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BAD_REVS = {'main', 'master', 'latest', ''}

def main() -> int:
    try:
       pin = json.loads((ROOT / 'encoder_pin.json').read_text())
    except FileNotFoundError:
       print('FAIL: encoder_pin.json missing')
       return 1
    except json.JSONDecodeError as e:
       print('FAIL: bad JSON', e)
       return 1
    eid = str(pin.get('encoder_id') or '').strip()
    rev = str(pin.get('revision') or '').strip()
    source = str(pin.get('source') or '').strip().lower()
    notes = str(pin.get('notes') or '').strip()
    if eid in ('', 'REPLACE_ME'):
       print('FAIL encoder_id')
       return 1
    if rev.lower() in BAD_REVS:
       print('FAIL revision must be a concrete pin, not main/master/latest')
       return 1
    if source == 'huggingface':
       if '/' not in eid:
           print('FAIL HF ids look like org/name')
           return 1
       if not notes:
           print('FAIL huggingface pins need notes describing the actual run or fallback')
           return 1
    if source == 'lab' or eid.startswith('lab-'):
       if 'honesty' not in {k.lower() for k in pin.keys()} and 'lab' not in notes.lower() and 'sidecar' not in notes.lower():
           # require an honesty field OR notes that admit the lab stub
           if 'honesty' not in pin:
                    print('FAIL lab encoder must set honesty (e.g. sidecar-tags) or notes admitting the stub')
                    return 1
       honesty = str(pin.get('honesty') or '').strip()
       if 'honesty' in pin and not honesty:
           print('FAIL empty honesty field')
           return 1
    print('encoder pin OK', eid, rev)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())