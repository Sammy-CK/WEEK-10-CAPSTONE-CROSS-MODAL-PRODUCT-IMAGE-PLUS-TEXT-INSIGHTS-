# Week 10: Advanced Multimodal AI (SokoniHub)

## Overview

SokoniHub cross-modal packet for four **teaching SKUs** (`n=4`): join listing **sidecar image tags** with title text, emit mismatch scores and `insights.json` (optional voice sidecar transcript on KND-01), optional campaign still-life under `outputs/` with provenance. **Join scores use `lab-bow-v1` sidecar tags, not CLIP pixels** — we say so explicitly for markers. AfyaPlus triage fixtures are not mixed here; poster/leaflet transfer is noted in `ethics_note.md`.

## Encoder honesty

- `encoder_pin.json`: **`lab-bow-v1`**, `honesty: sidecar-tags`, revision `sidecar-tags-v1`
- Did transformers run for **join**? **no** (optional `hf_pipeline.yaml` is Hub literacy only)

## Join

```bash
python mismatch.py
python check_mismatch.py
```

Gold pair: **KND-01 clear**, **NK-99 flagged** (bag/sisal tags vs Nike shoe title).

## Insights

```bash
python insights.py
python check_insights.py
```

Path: `insights.json` (no silent title rewrite in code).

## Tools

- `hf_pipeline.yaml` — CLIP task card (literacy only; **not** used for committed join scores)
- **DALL-E / SD / stub (circle one):** **DALL-E (OpenAI Images API)** — committed `outputs/knd-01_stilllife.png` + meta from local `render_stilllife.py` (`gpt-image-1`); **SD** listed as OSS twin in `gen_twin.json` (no fake checkpoint); **stub** used in **CI** via `stub_render.py`
- Provenance: `outputs/knd-01_meta.json`, `gen_pin.json`, `gen_twin.json`

```bash
python write_gen_pin.py
python render_stilllife.py   # local optional live image
python stub_render.py        # CI-safe stub
python check_gen_pin_starter.py
python check_outputs.py
```

## Analytics

- `rates.json` — quote **overall n=4** teaching slice
- `vocab_gaps.json` — title tokens outside lab VOCAB
- `search.py` + `search_note.md` — toy recall (`navy sisal kiondo` → KND-01)

```bash
python analytics_starter.py
python vocab_gaps.py
```

## Ethics

- [ethics_note.md](ethics_note.md) — four headings + manager summary
- Review path: flagged insights route to seller follow-up and moderators; no auto-takedown on bow score alone.

## Week reuse (1–9 habits)

- **Week 5:** CLIP as the multimodal idea; this submit uses **tags + bow** for join.
- **Week 7:** ~$0 join; optional DALL-E ~$0–0.20 if you run `render_stilllife.py` locally.
- **Week 8:** pins — `encoder_pin.json`, `gen_pin.json`, prompt file hash.
- **Week 9:** DPA-style people/face handling via `privacy_flag.py`; `.env` gitignored, no secrets in git.

## Fallbacks declared

- [x] no GPU / no transformers **for join scores**
- [x] no OpenAI image key **in CI** (stub); **local** OpenAI Images used once for committed still-life meta
- [x] no Whisper (audio `*.txt` sidecars)
- [x] n is a teaching slice (**four** SKUs, not production catalog)


## Checklist

- [x] NK-99 flagged, KND-01 clear
- [x] `outputs/` not mixed into gold `images/`
- [x] no overclaim language in ethics or seller messages
- [x] Weeks 5/7/8/9 reuse documented

## CI

```bash
pip install pytest
pytest -q
```

GitHub Actions: `.github/workflows/ci.yml`
