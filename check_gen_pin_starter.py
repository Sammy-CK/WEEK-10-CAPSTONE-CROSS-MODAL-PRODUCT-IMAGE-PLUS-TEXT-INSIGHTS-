import hashlib, json
from pathlib import Path

def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main() -> int:
    pin = json.loads(Path('gen_pin.json').read_text())
    path = Path(pin['prompt_file'])
    got = sha(path)
    if got != pin['sha256']:
        print('GEN PIN MISMATCH', got, pin['sha256'])
        return 1
    print('gen pin OK')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())