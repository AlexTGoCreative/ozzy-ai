"""
Review-suite runner for the Athena RAG mission.

For each question in data/evaluation/review_suite.json:
  1. POST it to the live /ask endpoint (the real system answer, with rerank +
     generation + abstention exactly as a user would see).
  2. (optional, default on) replay the SAME retrieve()+rerank() locally to log
     which source docs/sections won and their normalized rerank scores. This
     pinpoints retrieval-miss vs rerank-drop vs generation-fail.

Run INSIDE the ozzy-ai container (it can reach localhost:7860 and qdrant:6333):
    docker exec chatbot-ozzy-ai-1 python -m scripts.run_review --tag before
    docker exec chatbot-ozzy-ai-1 python -m scripts.run_review --tag after

Writes data/evaluation/review_results_<tag>.json and prints a compact table.
"""

import argparse
import json
import os
import sys
import time

import requests

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

API_URL = "http://localhost:7860"
EVAL_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "evaluation")
SUITE = os.path.join(EVAL_DIR, "review_suite.json")


def ask(question: str) -> dict:
    payload = {"chat_history": [{"role": "user", "text": question}]}
    t0 = time.time()
    try:
        r = requests.post(f"{API_URL}/ask", json=payload, timeout=180)
        dt = time.time() - t0
        if r.status_code != 200:
            return {"answer": f"ERROR {r.status_code}: {r.text[:200]}", "latency": dt}
        return {"answer": r.json().get("answer", ""), "latency": dt}
    except Exception as e:  # noqa
        return {"answer": f"EXCEPTION: {e}", "latency": time.time() - t0}


def diag(question: str, top: int = 8) -> list:
    """Replay retrieve()+rerank() to see which sources survive (raw query)."""
    from src.retrieval import retrieve
    from src.reranking import rerank

    candidates = retrieve(question)
    reranked = rerank(question, candidates)
    out = []
    for c in reranked[:top]:
        md = c.get("metadata", {}) or {}
        out.append({
            "source": md.get("source_url", "?"),
            "section": md.get("section_path", ""),
            "score": round(float(c.get("rerank_score", 0.0)), 4),
        })
    return {"n_candidates": len(candidates), "n_survivors": len(reranked), "top": out}


ABSTAIN_MARKERS = [
    "don't have enough", "do not have enough", "not enough information",
    "no relevant documentation", "can't help", "cannot help", "outside",
    "don't have specific documentation",
]


def looks_abstained(ans: str) -> bool:
    a = ans.lower()
    return any(m in a for m in ABSTAIN_MARKERS)


def main():
    global API_URL
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", default="run")
    ap.add_argument("--suite", default=SUITE, help="path to suite JSON (default review_suite.json)")
    ap.add_argument("--no-diag", action="store_true", help="skip local retrieval diagnostic")
    ap.add_argument("--api-url", default=API_URL)
    args = ap.parse_args()
    API_URL = args.api_url
    suite_path = args.suite if os.path.isabs(args.suite) else os.path.join(EVAL_DIR, os.path.basename(args.suite))

    with open(suite_path, encoding="utf-8") as f:
        suite = json.load(f)

    results = []
    print(f"Running {len(suite)} questions against {API_URL}  (diag={'off' if args.no_diag else 'on'})")
    print("=" * 100)
    for item in suite:
        q = item["question"]
        res = ask(q)
        d = None if args.no_diag else diag(q)
        ab = looks_abstained(res["answer"])
        results.append({**item, "actual": res["answer"], "latency": round(res["latency"], 2),
                        "abstained_heuristic": ab, "retrieval": d})
        top_src = ""
        if d and d["top"]:
            top_src = f'  win=[{d["n_survivors"]}surv] {d["top"][0]["source"]} ({d["top"][0]["score"]})'
        flag = "ABSTAIN" if ab else "ANSWER "
        print(f'Q{item["id"]:>2} [{item["category"][:6]:<6}] {flag} {res["latency"]:>5.1f}s{top_src}')
        print(f'      Q: {q[:90]}')
        print(f'      A: {res["answer"][:160].strip()}')
    print("=" * 100)

    out_path = os.path.join(os.path.dirname(SUITE), f"review_results_{args.tag}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    n_ab = sum(1 for r in results if r["abstained_heuristic"])
    print(f"Abstained (heuristic): {n_ab}/{len(results)}    Saved: {out_path}")


if __name__ == "__main__":
    main()
