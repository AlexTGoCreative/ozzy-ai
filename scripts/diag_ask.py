"""
Replicate the EXACT /ask pipeline for one question and print the intermediate
state: rewritten query, filters, the reranked sources, the doc_context block
headers + a preview of each block's parent_text, and the final generated answer.

This exposes whether a failure is retrieval (wrong docs), context-assembly
(parent_text dilution), or generation (model abstains on good context).

    docker exec chatbot-ozzy-ai-1 python -m scripts.diag_ask "What detection technologies does the Bitdefender engine use?"
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.query_rewrite import rewrite_query
from src.retrieval import retrieve
from src.reranking import rerank
from src.main import _extract_metadata_filters, _build_doc_context
from src.context import build_system_prompt
from src.generation import generate


def run(question: str):
    print("Q:", question)
    sq = rewrite_query(question, None)
    print("search_query:", repr(sq))
    filters = _extract_metadata_filters(sq)
    print("filters:", filters)

    candidates = retrieve(sq, filters=filters)
    reranked = rerank(sq, candidates)
    print(f"\ncandidates={len(candidates)}  reranked={len(reranked)}")

    doc_context = _build_doc_context(reranked)
    print("\n===== doc_context blocks (header + first 220 chars of parent_text) =====")
    for i, c in enumerate(reranked):
        md = c.get("metadata", {}) or {}
        ptext = c.get("parent_text", c.get("text", ""))
        print(f"\n[{i+1}] score={c.get('rerank_score'):.4f}  src={md.get('source_url')}  sec={md.get('section_path')}")
        print("    parent_text[:220]:", " ".join(ptext[:220].split()))

    scan_context = ""
    system_prompt = build_system_prompt(doc_context, scan_context)
    print("\n===== system_prompt length:", len(system_prompt), "chars =====")

    msgs = [{"role": "developer", "content": system_prompt},
            {"role": "user", "content": question}]
    ans = generate(msgs)
    print("\n===== ANSWER =====")
    print(ans)


if __name__ == "__main__":
    run(sys.argv[1] if len(sys.argv) > 1 else "What detection technologies does the Bitdefender engine use?")
