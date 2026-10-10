import json
from pathlib import Path

from mismatch import bow, cosine, tokens

ROOT = Path(__file__).resolve().parent


def search(query, catalog, k=3):
    qv = bow(tokens(query))
    scored = []
    for row in catalog:
        iv = bow(row.get('image_tags') or [])
        scored.append((cosine(qv, iv), row['sku']))
    scored.sort(reverse=True)
    return scored[:k]


if __name__ == '__main__':
    catalog = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))
    results = search('navy sisal kiondo', catalog, k=3)
    assert results[0][1] == 'KND-01', results
    print("search('navy sisal kiondo') top-k =", results)
