"""Write tiny valid JPEG placeholders for catalog image paths (not generated campaign art)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IMAGES = ROOT / 'images'
NAMES = ['knd-01.jpg', 'nk-99.jpg', 'bag-mid.jpg', 'lso-02.jpg']

# 1x1 grey JPEG — teaching fixture only (no marketplace crawl).
MINIMAL_JPEG = (
    b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00'
    b'\xff\xdb\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c\x1c $.\' ",#\x1c\x1c(7),01444\x1f\'9=82<.342'
    b'\xff\xc0\x00\x0b\x08\x00\x01\x00\x01\x01\x01\x11\x00\xff\xc4\x00\x14\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08'
    b'\xff\xc4\x00\x14\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?\x00\xaa\xff\xd9'
)


def minimal_jpeg() -> bytes:
    return MINIMAL_JPEG


def main() -> int:
    IMAGES.mkdir(parents=True, exist_ok=True)
    data = minimal_jpeg()
    for name in NAMES:
        (IMAGES / name).write_bytes(data)
    print('wrote', len(NAMES), 'fixture images under images/')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
