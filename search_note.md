# Search helper (toy recall)

`search.py` ranks SKUs by cosine between a query bag-of-words and each row's **sidecar `image_tags`** (same VOCAB as `mismatch.py`).

Example on the committed catalog:

```text
python search.py
```

Expected top match for query `navy sisal kiondo` is **KND-01** (tags include navy, sisal, kiondo). This is **toy recall** on four teaching rows only (`n=4`), not production search quality.
