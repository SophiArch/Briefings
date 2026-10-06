# Evaluating LLMs & Agents (part 1 of 2)

Builds an evaluation harness for a bank's document-grounded customer assistant, and asks
"which grader can we trust, and how do we know?"

## Contents

| File | What it is |
|------|------------|
| `../Evaluating_LLMs_and_Agents.md` | Marp deck with speaker notes and timings (~88 min, plus a 10-min break slide) |
| `llm_eval_harness.ipynb` | Hands-on notebook: exact match → rules → similarity → LLM judge → agreement with humans → release gate |
| `data/eval_testset.csv` | 26 test cases: answerable (A01–A17), must refuse (R1–R5), withheld documents (W1–W4) with reference answers, must / must-not rules, sources, dev/test split |
| `data/agent_responses.csv` | Responses from two builds: **v1** (superseded docs indexed, no refusal rules) and **v2** (after audit and instructions) |
| `data/human_labels.csv` | Reference pass/fail labels and failure modes from a human reviewer (ground truth) |
| `data/judge_cache.csv` | Sample LLM-judge verdicts for offline use. Written for teaching (illustrative, not captured from a model run), with 4 deliberate disagreements |
| `../Images/` | Diagrams used in the deck |

## Running the notebook

- Colab: use the badge at the top of the notebook (data loads from GitHub)
- Local: needs pandas, matplotlib, scikit-learn and pydantic (e.g. `uv run --with scikit-learn --with pydantic --with jupyterlab jupyter lab`), then open the notebook from this folder (data loads from `./data`)
- Default `JUDGE_MODE = "cached"` needs no keys. For a live judge: `pip install anthropic`, then set
  - `JUDGE_MODE = "anthropic"` with `ANTHROPIC_API_KEY`, or
  - `JUDGE_MODE = "foundry"` with `ANTHROPIC_FOUNDRY_API_KEY` and `ANTHROPIC_FOUNDRY_RESOURCE` (Claude deployed in Microsoft Foundry)

## Answer key (what participants should find)

| Grader | Agreement with humans | Cohen's κ | Lesson |
|--------|-----------------------|-----------|--------|
| Exact match | 40% | 0.00 | Useless for free text |
| Similarity (TF-IDF) | 75% | 0.49 | `$2.00` and `$5.00` tokenise identically; topic ≠ truth |
| LLM judge (cached) | 92% | 0.84 | Lenient on omissions (A02 v1, A11 v1, A16 v2); too literal on R5 v2 |
| Rules | 100% | 1.00 | Flattered: same author wrote the rules and the labels |

Release gate on the test split: v1 33% pass with 5 critical failures, v2 89% pass with 0 critical. Both are **BLOCK** at a 90% threshold.
