# Athena RAG — Future Work

Deferred, non-blocking improvements for the Athena RAG knowledge base and retrieval
pipeline. As of 2026-06-21 the review suites pass: **20/20** on the AGATHA + MetaDefender +
engines suite (`data/evaluation/review_suite.json`) and **10/10** on the MetaDefender
Community-Edition suite (`data/evaluation/review_suite_mdcore.json`). Full history:
`_rag_eval_report.md`. Background on the parent-linkage root-cause fix and the eval loop:
the `ozzy-rag-parent-linkage-fix` memory.

## How to run the eval loop (recap)
Services are NOT host-exposed — run inside the container. After editing docs in the
bind-mounted `data/scraped/` (and `docker cp` any changed `src/` file into the container):
```
docker exec chatbot-ozzy-ai-1 python -m scripts.ingest --from-disk --rebuild
docker exec chatbot-redis-1 redis-cli FLUSHALL          # MUST flush, else stale cached answers
docker exec chatbot-ozzy-ai-1 python -m scripts.run_review --tag <t>
docker exec chatbot-ozzy-ai-1 python -m scripts.run_review --suite review_suite_mdcore.json --tag <t>
```
`scripts/diag_ask.py "<question>"` prints the actual retrieved context blocks + answer
(use it to distinguish retrieval-miss vs parent-text vs generation issues).

## Deferred items

### 1. Recover truncated scan-result code descriptions (codes 26–28)
`data/scraped/docs_mdcore_integration.md` — the descriptions for scan-result codes 26, 27,
and 28 (Sandbox Suspicious / Likely Malicious / Malicious UI strings) were cut off by the
original scraper ("…the Core UI will display"). Re-fetch the full text from
`https://www.opswat.com/docs/mdcore/integration/description-of-scan-result-codes` (WebFetch)
and complete those three rows. Low value (sandbox UI strings), low effort.

### 2. Index the MetaDefender Cloud API content (improve the legacy golden_set)
The older `data/evaluation/golden_set.json` (30 Qs on the MetaDefender **Cloud API**: hash
lookup, scan-result codes, Deep CDR, reputation, sandbox, API-key tiers) is only crudely
scored (Jaccard in `scripts/evaluate.py`) and partly depends on content that is **not
indexed**: the ingester (`scripts/ingest.py _load_from_disk`) globs `*.md` only, so
`data/scraped/hash_lookup.txt` and `data/scraped/explanations.txt` are never retrievable.
To improve that suite, extract their unique content into indexed `.md` docs, e.g.:
- `docs_mdcloud_hash-lookup-api.md` — GET/POST hash lookup, bulk hash lookup, scan history, file badge.
- `docs_mdcloud_api-key-tiers.md` — API-key limits, qos/throttling, free vs paid tiers, rate-limit headers.
- `docs_mdcloud_scan-result-codes.md` — the user-facing per-code guidance prose from `explanations.txt`
  (incl. code 5 "Unknown"/bulk and code 11 "Aborted"), which is richer than the table rows.
Then re-ingest and re-run. (Code 5 is already in `docs_mdcore_integration.md`; code 11 is not.)

### 3. Optional retrieval/grading upgrades
- `scripts/evaluate.py` uses token-overlap (Jaccard) scoring — replace with an LLM-judge or
  embedding cosine for the golden_set, matching the quality of the manual grading used for
  the review suites.
- `run_review.py`'s abstention heuristic misses curly-apostrophe refusals ("can't") — cosmetic;
  the actual abstention behavior is correct. Tighten the marker list if the counter matters.

### 4. Make the code fixes permanent in the image
The parent-linkage fix lives in host `src/ingestion/chunker.py` and the eval scripts live in
host `scripts/` + `data/evaluation/` — all included on `docker compose build ozzy-ai`. If the
container is ever recreated without a rebuild, re-`docker cp` `src/ingestion/chunker.py`
before ingesting. No `src` config change (RERANK_THRESHOLD / top-k) was needed.

### 5. (If ever desired) per-doc content_hash header in the loader
`scripts/ingest.py _load_from_disk` parses `source_url`/`product`/`doc_type` from the HTML
comment header but ignores the optional `<!-- content_hash -->` line. The chunker now derives
a stable per-chunk hash itself, so this is not required — but wiring the doc-level header
through would give deterministic dedup keyed on the author-stamped hash if that's ever wanted.
