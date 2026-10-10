import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from mismatch import score_row
from privacy_flag import needs_privacy_review


def transcript_for(sku: str) -> str:
    p = ROOT / 'audio' / (sku.lower() + '.ogg.txt')
    return p.read_text(encoding='utf-8').strip() if p.exists() else ''


def insight(row, scored):
    if scored['flag']:
        sent = (
            'Your photo tags and title disagree (e.g. bag tags vs shoe title). '
            'Please retake the photo or fix the title; moderators will review.'
        )
    else:
        sent = 'Photo tags and title look aligned for this listing.'
    out = {
        'sku': row['sku'],
        'score': scored['score'],
        'flag': scored['flag'],
        'seller_message': sent,
        'transcript': row.get('transcript') or transcript_for(row['sku']),
    }
    if needs_privacy_review(row.get('image_tags')):
        out['needs_privacy_review'] = True
    return out


if __name__ == '__main__':
    path = ROOT / 'catalog.json'
    try:
        rows = json.loads(path.read_text(encoding='utf-8'))
    except FileNotFoundError:
        print('FAIL: catalog.json missing. Keep insights.py beside catalog.json.')
        raise SystemExit(1)
    except json.JSONDecodeError as e:
        print('FAIL: catalog.json JSON error:', e)
        raise SystemExit(1)
    pack = [insight(r, score_row(r)) for r in rows]
    (ROOT / 'insights.json').write_text(json.dumps(pack, indent=2) + '\n', encoding='utf-8')
    print('wrote insights.json', len(pack))
