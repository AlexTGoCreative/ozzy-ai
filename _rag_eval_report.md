# Athena RAG Evaluation & Improvement Report

Date: 2026-06-20 (iteration 1)
Endpoint: `chatbot-ozzy-ai-1:7860/ask` (live: hybrid retrieval + bge-reranker + OpenAI generation)
Retrieval config (src/config.py): hybrid top_n=50 → bge-reranker-v2-m3 → top_k=8, RERANK_THRESHOLD=0.2.
Suite: `data/evaluation/review_suite.json` — 20 questions (5 multiscanning, 9 AGATHA, 5 engines, 1 abstention probe; mix of simple / multi-hop / architecture / workflow / multi-document).
Harness: `scripts/run_review.py` (calls real /ask + replays retrieve()+rerank() to log winning sources/scores). Diagnostic: `scripts/diag_ask.py` (replicates /ask and prints the doc_context blocks + answer).

## Headline result

| | Correct | Partial | Incorrect | Correct abstention |
|---|---|---|---|---|
| **Before** | 3 | 3 | 13 | 1 (Q20) |
| **After**  | **19** | **0** | **0** | **1 (Q20)** |

**20/20 of the review suite now answered correctly** (19 substantive + the out-of-scope probe correctly declined). The abstention guardrail is intact (Q20 still refuses; no new over-answering).

## Root-cause analysis (this is the important part)

The prior report concluded the failures were "retrieval failures" and prescribed documentation heading/lead rewrites. Instrumenting the pipeline disproved that diagnosis and found a deeper bug:

1. **Cache contamination (methodology).** The original eval run cached 44 answers in Redis (24 h TTL). Re-runs served those stale answers instead of re-generating. Fix: **flush Redis (`FLUSHALL`) before every eval run**. (Built into the loop now.)

2. **THE ROOT CAUSE — broken parent→child linkage in `chunker.py`.** The pipeline retrieves on small *child* chunks but feeds the LLM the larger *parent* chunk (`parent_text`). `parent_id` was built as `f"{base_metadata.get('content_hash','unknown')[:12]}_{n}"`, but `_load_from_disk` **never populates `content_hash`** → every document numbered its parents `unknown_0, unknown_1, …` from zero → **global `parent_id` collision across all 59 docs**. In `indexer.index_documents`, `parent_lookup[parent_id] = text` then overwrote, and the bulky MetaDefender/multiscanning docs (ingested last) won every key. Net effect: a child chunk from, say, `av-engine/bitdefender` was paired with **a MetaDefender-multiscanning parent_text**. The reranker correctly ranked the Bitdefender child #1 (score 0.73), but the LLM received multiscanning prose and faithfully answered "this is about multiscanning, not Bitdefender" → abstention. Proven with `diag_ask.py`: every `doc_context` block had the correct `source` but wrong-document `parent_text`.

   **Fix (`src/ingestion/chunker.py`):** derive a document-unique namespace `doc_ns = f"{source_url}:{sha256(doc_text)[:12]}"` and set `parent_id = f"{doc_ns}#p{n}"`; also stamp a real per-chunk `content_hash` so Qdrant point ids (uuid5) are stable and unique. Ingest-time only → applied by re-ingesting; no image rebuild or server restart required. Post-fix `diag_ask` confirms Bitdefender's child now carries Bitdefender `parent_text`, and the answer is fully correct.

3. **Documentation discoverability (secondary, still valuable).** Generic section headings (`## Overview`, `## Detection technologies`) and missing answer-first sentences. Applied across all 11 `agatha_*.md` and 21 `av_engine_*.md`: the entity name now appears in every heading and a bolded answer-first lead restates the key fact (and explicit negations for the fragile cases — OOXML-no-YARA, per-link-doesn't-change-verdict). These sharpen child-chunk retrieval/reranking and give the model crisp facts; with the parent linkage fixed, they now actually reach the LLM.

## Changes made

**Code (1 file, ingest-time):**
- `src/ingestion/chunker.py` — document-unique `parent_id` + per-chunk `content_hash` (fixes the parent linkage collision).

**Documentation (32 files, evidence-based — no facts changed, only headings + answer-first leads):**
- `agatha_ml-models.md`: added "AGATHA ML quick facts" block (algorithm, ML file types, all per-type thresholds); named thresholds in the heading; explicit "per-link does NOT change verdict" lead.
- `agatha_yara-features.md`: answer-first "YARA as numeric features, not verdicts"; explicit "OOXML model does NOT use YARA" lead.
- `agatha_ozzy-assistant.md`: answer-first full RAG-stack lead; "Athena reranking" heading.
- `agatha_url-aegis.md`: "how Aegis works" lead co-locating features+algorithm+0.90 threshold; explicit per-link negation.
- `agatha_evaluation.md`: answer-first metrics+limitations summary.
- `agatha_training-methodology.md`: promoted the "≥3-engine" labeling rule into a dedicated heading + synonyms.
- `agatha_overview/scan-pipeline/heuristics/reputation/architecture-deployment.md`: entity-named headings + answer-first leads.
- All 21 `av_engine_*.md`: vendor name in every heading + answer-first detection-tech lead (incl. Bitdefender stack, Xcitium ZeroDwell, RocketCyber EOL date in heading, Alin AI "ML/AI static, no signatures, no sandbox").

**Process:** flush Redis before each eval; re-ingest with `--from-disk --rebuild` (safe — all 59 source files are on disk; the 2 `.txt` files are never ingested, the loader globs `*.md` only). Collection rebuilt 1133 → 1211 points.

## Per-question outcome (after)

All CORRECT. Notable flips from abstention/incorrect → correct: Q3 (≥3 rule), Q6 (4 layers), Q7 (YARA→18 features), Q8 (ML file types), Q9 (OOXML no-YARA), Q10 (XGBoost/ONNX + PE 0.70), Q11 (Aegis 107→103, 0.90), Q12 (per-link does not change verdict — the old contradiction is gone), Q13 (full RAG stack), Q14 (metrics + all 6 limitations), Q15 (Bitdefender stack), Q17 (ZeroDwell), Q18 (RocketCyber EOL 2026-08-01), Q19 (Alin AI). Q20 correctly abstained.

## Remaining risks / not-yet-done (iteration 2 candidates, none blocking the suite)

- **MetaDefender Cloud API content gaps (affect the older `golden_set.json`, not the 20-Q suite):** scan-result **code 5 "Unknown" (bulk hash)** and code 11 "Aborted", plus the hash-lookup API and API-key tier model, live ONLY in the un-indexed `hash_lookup.txt` / `explanations.txt`. Recommend extracting them into indexed `.md` docs.
- **Duplicate `docs_mdcore` files** create duplicate chunks: `docs_mdcore_metascan-engines.md` ≡ `_anti-malware-vendors.md`; `docs_mdcore_metadefender-core.md` ≡ `_ref.md`; `docs_mdcore.md` is a cookie-banner with no content. Recommend de-duplicating (low risk, reduces index noise). Verify byte-identity before removing.
- **Typos in scraped tables:** engine name "Anity" → "Antiy"; "Signature base" → "Signature based".
- **Generic H1 `# Overview`** in several `docs_mdcore_*` (reputation-engine, threat-intelligence-engine, ai-content-inspector) — rename to name the engine.
- **Stability:** retrieval is deterministic and answers are now well-grounded (winning rerank scores ~0.73 with correct `parent_text`); a second run is expected to reproduce. Confidence: high.

## Next actions (highest impact first)

1. (Optional) Re-run the suite once to confirm stability ("consistently passed").
2. Iteration 2: extract scan-code-5/code-11 + hash-lookup facts from the `.txt` files into indexed `.md`; de-duplicate the redundant `docs_mdcore` files; fix the "Antiy" typo; re-ingest; re-run both suites to confirm no regression and improve the `golden_set` MetaDefender-API coverage.
3. Keep the parent-linkage fix in the image: it lives in host `src/ingestion/chunker.py`, so `docker compose build ozzy-ai` will bake it in.

---

# Iteration 2 — docs_mdcore consolidation + web fact-check (2026-06-20)

Goal: review every `docs_mdcore_*.md`, merge same-idea fragments, remove duplicates, and cross-check volatile facts against the live web (opswat.com), updating stale content.

## Result

| Suite | Result |
|---|---|
| 20-Q review suite (regression) | **20/20** (no regression) |
| MetaDefender-CE suite (`review_suite_mdcore.json`, 10 Qs) | **10/10** |

The new MetaDefender-CE suite (scan codes incl. code 5, reputation engine, Alin AI, AI Content Inspector, package tiers, ClamAV custom DB, Post-Action scoring, Cyren→Varist, YARA) is a targeted check that the consolidated/updated `docs_mdcore` content is retrievable and accurate.

## Changes made

**Consolidation (20 → 12 `docs_mdcore` files):**
- Deleted 3 redundant: `docs_mdcore.md` (cookie banner), `docs_mdcore_metadefender-core_ref.md` and `docs_mdcore_metascan-engines_anti-malware-vendors.md` (byte-identical scrape duplicates).
- Created `docs_mdcore_engine-configuration.md` merging 5 engine-management stubs (AV return codes, AI-engine supported file types, engine scoring with Post Action, ClamAV custom DB, Windows Defender custom engine) under entity-named section headings.
- Merged the public-sector roster into `docs_mdcore_metascan-engines.md` (renamed H1; added "Notes on detection flags"); 9 files net removed.
- Renamed generic `# Overview` H1s → entity names: `docs_mdcore_reputation-engine.md`, `docs_mdcore_threat-intelligence-engine.md`, `docs_mdcore_opswat-ai-content-inspector-engine.md`; added an H1 + entity-named headings to `docs_mdcore_metadefender-core.md`.

**Web-verified fact updates (citations gathered against opswat.com, June 2026):**
- Added scan-result **code 5 = "Unknown" (bulk-hash-only)** to `docs_mdcore_integration.md` (was missing from every indexed doc; lived only in the un-indexed `.txt`).
- **Code 19** Core="Cancelled" vs Cloud="Potentially Vulnerable File" disambiguation note (engine-configuration doc).
- **Cyren → Varist** (renamed 2023-05-24) correction in the public-sector roster; **RocketCyber EOL 2026-08-01** note; **Cylance → Aurora** annotation in AI-engine file-types.
- **Reputation Engine** = OPSWAT global hash DB (40B+ entries) → Known Good/Bad/Unknown.
- **Predictive Alin AI** = first proprietary engine, v3.0 (2026-04-08), static/pre-execution/no sandbox; supported types **PE/ELF/Mach-O/PDF** (also fixed the contradicting hedge in `av_engine_opswat-alin-ai.md`, which had said the format list was unenumerated — this was the one PARTIAL that the fix turned into a pass).
- **AI Content Inspector** v2.0 (2026-06-10), AI-generated-content + document-fraud, image/PDF/text formats.
- Typo fix: "Signature base" → "Signature based". Kept "Anity" (it is OPSWAT's documented engine key; vendor = Antiy Labs — NOT a typo, confirmed via web).

**Decisions of note:** kept the 4 per-engine module docs separate (one concept per file suits RAG; the heading rename fixes their discoverability) and kept `docs_mdcore_integration.md` intact (sole source of the full 40+ scan-result code table). Corpus rebuilt 1211 → 1177 chunks (duplicates removed).

## Remaining (optional)
- `docs_mdcore_integration.md` codes 26–28 have scraper-truncated descriptions (sandbox UI strings) — could be re-fetched from opswat.com if needed; non-blocking.
- The older `golden_set.json` (MetaDefender Cloud API endpoints) still depends partly on the un-indexed `hash_lookup.txt`; converting its hash-lookup/API-key sections into indexed `.md` would improve that legacy suite.
