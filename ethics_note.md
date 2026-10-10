# SokoniHub multimodal ethics note (teaching slice, n=4 SKUs)

## Who is in the photos

Listing fixtures use sidecar tags and tiny placeholder JPEGs in `images/`, not a crawl of marketplace faces. Tags that include person, face, or child set `needs_privacy_review` via `privacy_flag.py`; we do not commit real child photos. Personal data in photos follows the same DPA habits as Week 9: minimise collection, restrict access, and delete on valid erasure requests.

## Whose language

The lab VOCAB is small English and drops Kenyan product words (kiondo, leso, sisal). `vocab_gaps.json` lists missing title tokens so managers see coverage limits. We will not silently rewrite seller titles into US English just to inflate cosine scores.

## Generated pixels

Campaign still-lifes live under `outputs/` with `not_a_photo_of_the_sku: true` in meta JSON. They are marketing aids only and never replace NK-99 or KND-01 gold listing paths. Prompts forbid people and sportswear logos; we do not use generation to fabricate proof of authenticity.

## Review path

Low join scores flag a row for seller follow-up and moderator review. There is no automatic takedown from bag-of-words alone and no silent title overwrite in code. Escalations log SKU, score, and seller_message for a human decision.

## Manager summary

**Risks:** title–photo mismatch (counterfeit or careless listings), vocabulary bias against local product names, and misuse of generated still-lifes as if they were seller photos. **Mitigations:** sidecar-tagged teaching catalog, honest encoder pin (`lab-bow-v1`), flagged insights with plain seller copy, privacy tags, and separated `outputs/` provenance. **We will not claim** that scores prove Nike authenticity, that the pipeline is perfectly secure, or that generated art is the SKU photo. AfyaPlus poster/leaflet multimodal work transfers later; AfyaPlus triage fixtures are not mixed into this SokoniHub catalog.
