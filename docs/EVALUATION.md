# RAG Evaluation

## Overview

The evaluation suite measures the quality of the RAG pipeline using a golden set of question-answer pairs. It tests retrieval precision, answer correctness, and abstention behavior.

## Running Evaluation

```bash
python scripts/evaluate.py
```

Results are written to `data/evaluation/results_<timestamp>.json`.

## Golden Set

Located at `data/evaluation/golden_set.json`. Each entry contains:

```json
{
  "question": "What does verdict code 1 mean?",
  "expected_answer": "Verdict 1 indicates the file is clean/not detected.",
  "expected_source": "hash_lookup",
  "category": "verdict_codes"
}
```

### Categories

| Category | Description |
|----------|-------------|
| `verdict_codes` | Scan verdict interpretation |
| `api_usage` | MetaDefender API endpoints and parameters |
| `scan_results` | Interpreting scan result fields |
| `general` | General cybersecurity questions |
| `out_of_scope` | Questions the system should abstain on |

## Metrics

| Metric | Definition |
|--------|-----------|
| **Retrieval Precision@5** | Fraction of top-5 retrieved docs that are relevant |
| **Answer Correctness** | Semantic similarity between generated and expected answer |
| **Abstention Rate** | % of out-of-scope questions where model correctly acknowledges lack of knowledge |
| **Latency P50/P95** | End-to-end response time percentiles |

## Evaluation Methodology

1. **Retrieval Quality:** For each golden question, retrieve + rerank documents. Check if relevant source appears in top-5.
2. **Generation Quality:** Compare generated answer against expected answer using embedding cosine similarity (threshold ≥ 0.7 = correct).
3. **Abstention:** For out-of-scope questions, verify the response includes uncertainty language.
4. **Performance:** Record per-stage and total latency.

## Extending the Golden Set

Add entries to `data/evaluation/golden_set.json` following the schema above. Aim for:
- At least 5 questions per category
- Clear, unambiguous expected answers
- Both in-scope and out-of-scope questions
