# 1:1 defense cheat sheet (SokoniHub Week 10)

Use this order if the reviewer asks “walk me through it.”

## 30-second pitch

SokoniHub packet for **four teaching SKUs** (`n=4`, not production). We **join listing text with image sidecar tags**, score agreement, emit **insights** for sellers, optional **voice sidecar** transcript, optional **campaign still-life** with provenance, **rates** for managers, and an **ethics note**. AfyaPlus triage fixtures are **not** in this catalog.

## If they ask: “Two SKUs? CLIP?”

- We have **four SKUs**: KND-01, NK-99, BAG-MID, LSO-02 (`catalog.json`).
- **Join scores use sidecar tags + `lab-bow-v1` bag-of-words**, not CLIP on pixels — stated in `encoder_pin.json` and README.
- `hf_pipeline.yaml` is **optional Hub literacy**; transformers did **not** produce `mismatch_report.json`.

## Deliverable 1 — Join (demo)

```bash
python mismatch.py
python check_mismatch.py
```

- **KND-01 clear** (kiondo title matches tags).
- **NK-99 flagged** (bag/sisal tags vs Nike shoe title).
- Threshold in `mismatch.py`; pin matches scorer: **`lab-bow-v1`**.

## Deliverable 2 — Insights

- `insights.json`: score, flag, **seller_message** (no silent title rewrite in `insights.py`).
- **KND-01** has `transcript` from `audio/knd-01.ogg.txt` (no Whisper).

## Deliverable 3 — HF / generation

- **Generation (circled path): OpenAI Images** (`gpt-image-1` locally) with `gen_pin.json`, prompt file, `outputs/knd-01_meta.json` (`not_a_photo_of_the_sku: true`).
- **OSS twin:** Stable Diffusion named in `gen_twin.json` — we did not fake a checkpoint.
- **CI** runs `stub_render.py` so GitHub needs no API key; repo commits **live meta + still-life** from local run.

## Deliverable 4 — Analytics

- `rates.json`: **overall n=4**, flag_rate 0.25 (one flagged SKU).
- `vocab_gaps.json`: title tokens outside small VOCAB.
- `search.py` + `search_note.md`: toy recall query → KND-01.

## Deliverable 5 — Ethics

- `ethics_note.md`: four headings + **manager summary** (risks, mitigations, no overclaim).
- `privacy_flag.py`: person/face/child tags → review.
- **AfyaPlus posters later**; fixtures not mixed.

## Week habits (1–9 transfer)

| Week | What we reused |
|------|----------------|
| 5 | CLIP as multimodal *idea*; honest tag encoder for teaching slice |
| 7 | ~$0 join; one optional image gen call (~cents) |
| 8 | `encoder_pin.json`, `gen_pin.json`, prompt hash |
| 9 | DPA-style people handling; `.env` gitignored |

## What we do **not** claim

- Scores do **not** prove Nike authenticity.
- Generated still-life is **not** the seller listing photo.
- No auto-takedown from bow score alone.

## Automated evidence

```bash
pytest -q
```

GitHub Actions workflow `ci-week10` on `main` after push.
