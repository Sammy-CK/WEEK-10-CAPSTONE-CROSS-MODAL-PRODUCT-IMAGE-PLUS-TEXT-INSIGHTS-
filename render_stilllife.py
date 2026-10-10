"""Campaign still-life: DALL-E when OPENAI_API_KEY is set locally; else stub PNG + same meta shape."""
import hashlib
import json
import os
import struct
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROMPT = ROOT / 'prompts' / 'gen' / 'kiondo_lifestyle_v1.txt'
OUT = ROOT / 'outputs'
SKU = 'KND-01'


def load_dotenv_local() -> None:
    env_path = ROOT / '.env'
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, _, val = line.partition('=')
        os.environ.setdefault(key.strip(), val.strip())


def prompt_sha256() -> str:
    return hashlib.sha256(PROMPT.read_bytes()).hexdigest()


def write_stub_png(path: Path) -> None:
    def chunk(tag, data):
        return (
            struct.pack('>I', len(data))
            + tag
            + data
            + struct.pack('>I', zlib.crc32(tag + data) & 0xFFFFFFFF)
        )

    raw = zlib.compress(b'\x00' + bytes([0, 0, 255]))
    png = (
        b'\x89PNG\r\n\x1a\n'
        + chunk(b'IHDR', struct.pack('>IIBBBBB', 1, 1, 8, 2, 0, 0, 0))
        + chunk(b'IDAT', raw)
        + chunk(b'IEND', b'')
    )
    path.write_bytes(png)


def render_dalle(path: Path) -> dict:
    from openai import OpenAI

    client = OpenAI()
    prompt = PROMPT.read_text(encoding='utf-8').strip()
    attempts = [
        ('gpt-image-1', '1024x1024'),
        ('dall-e-3', '1024x1024'),
        ('dall-e-2', '512x512'),
    ]
    resp = None
    model = attempts[0][0]
    last_err = None
    for model, size in attempts:
        try:
            resp = client.images.generate(model=model, prompt=prompt, size=size, n=1)
            break
        except Exception as exc:
            last_err = exc
            resp = None
    if resp is None:
        raise last_err or RuntimeError('Images API unavailable')
    import base64
    import urllib.request

    item = resp.data[0]
    if getattr(item, 'b64_json', None):
        path.write_bytes(base64.b64decode(item.b64_json))
    elif getattr(item, 'url', None):
        urllib.request.urlretrieve(item.url, path)
    else:
        raise RuntimeError('No image payload from Images API')
    return {
        'generator': model,
        'request_id': getattr(resp, 'id', None) or getattr(resp, '_request_id', None),
    }


def main() -> int:
    if not PROMPT.exists():
        print('FAIL prompt file missing:', PROMPT)
        return 1
    OUT.mkdir(parents=True, exist_ok=True)
    load_dotenv_local()
    sha = prompt_sha256()
    meta = {
        'sku': SKU,
        'format': 'png',
        'prompt_file': str(PROMPT.relative_to(ROOT)).replace('\\', '/'),
        'prompt_sha256': sha,
        'not_a_photo_of_the_sku': True,
    }
    api_key = os.environ.get('OPENAI_API_KEY', '').strip()
    out_png = OUT / 'knd-01_stilllife.png'
    if api_key:
        try:
            extra = render_dalle(out_png)
            meta.update(extra)
            print('wrote live OpenAI still-life (campaign only, not catalog gold)')
        except Exception as exc:
            print('WARN DALL-E failed, using stub:', exc)
            write_stub_png(out_png)
            meta['generator'] = 'stub'
            meta['fallback_reason'] = str(exc)[:200]
    else:
        write_stub_png(out_png)
        meta['generator'] = 'stub'
        meta['fallback_reason'] = 'OPENAI_API_KEY not set'
        print('wrote stub still-life (set OPENAI_API_KEY locally for live DALL-E)')
    meta_path = OUT / 'knd-01_meta.json'
    meta_path.write_text(json.dumps(meta, indent=2) + '\n', encoding='utf-8')
    print('meta:', meta_path)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
