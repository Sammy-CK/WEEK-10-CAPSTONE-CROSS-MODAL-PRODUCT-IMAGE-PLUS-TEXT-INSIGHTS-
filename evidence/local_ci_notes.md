# Local verification

Run from repo root:

```bash
python make_fixture_images.py
python mismatch.py && python check_mismatch.py
python analytics_starter.py && python vocab_gaps.py
python insights.py && python check_insights.py
python write_gen_pin.py
python render_stilllife.py
python check_gen_pin_starter.py && python check_outputs.py
python check_encoder_pin.py && python check_ethics.py
python check_gitignore.py && python search.py
pytest -q
```

Optional live DALL-E requires `OPENAI_API_KEY` in local `.env` (never committed).
