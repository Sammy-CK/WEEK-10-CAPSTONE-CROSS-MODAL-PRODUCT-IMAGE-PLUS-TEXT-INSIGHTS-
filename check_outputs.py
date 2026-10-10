"""Generated campaign art must stay under outputs/, not images/."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> int:
    meta = ROOT / 'outputs' / 'knd-01_meta.json'
    if not meta.exists():
        print('FAIL: missing outputs/knd-01_meta.json — run render_stilllife.py or stub_render.py')
        return 1
    data = json.loads(meta.read_text(encoding='utf-8'))
    if not data.get('not_a_photo_of_the_sku'):
        print('FAIL: meta must set not_a_photo_of_the_sku')
        return 1
    gold = ROOT / 'images'
    for name in ('knd-01_stilllife.png', 'knd-01_stub.png'):
        if (gold / name).exists():
            print('FAIL: generated file in images/:', name)
            return 1
    print('outputs provenance OK')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
