# AI Agent as Data Scientist (extra session, part 2 of 2)

A coding agent builds a fraud model from a one-line brief and reports "98.9% accuracy, ready for production".
Students review its work like a pull request, find the leakage, and rewrite the brief.

## Contents

| File | What it is |
|------|------------|
| `../AI_Agent_as_Data_Scientist.md` | Marp deck with speaker notes and timings (~82 min) |
| `briefs/brief_v1.md` | The one-line brief for the live demo, and why it is weak |
| `briefs/brief_v2.md` | A brief written like a spec (goal, evidence rules, deliverables, escalation) |
| `review_checklist.md` | Student checklist: reproduce, data, split, metrics, claims, verdict |
| `agent_v1_output.ipynb` | Fallback "agent output" to review. A reconstruction of typical agent work, written for this class; numbers are real |
| `reference_review.ipynb` | Instructor answer key: duplicates, baseline, card-level leakage, business metric |
| `../Images/` | Diagrams used in the deck |

Both notebooks load the Milestone 8 `fraud_dataset.csv` from GitHub, so they run in Colab with no setup.

## Instructor prep

1. Have a coding agent ready (Claude Code, GitHub Copilot agent mode, Colab Data Science Agent, or Copilot in Fabric)
2. Keep `briefs/brief_v1.md` open to paste. Don't improvise the wording
3. Open `agent_v1_output.ipynb` as the fallback if the network or agent misbehaves
4. Keep `reference_review.ipynb` closed until groups have reported

## Answer key

| Setup | Accuracy | Baseline | Recall (count) | Precision | Recall (by $ value) |
|-------|----------|----------|----------------|-----------|---------------------|
| Agent: random split, as given | 98.9% | 50.0% | 99.5% | 98.3% | 100.0% |
| Deduplicated, random split | 97.1% | 76.3% | 89.6% | 98.0% | 98.4% |
| Deduplicated, split by card | 96.2% | 78.4% | 84.5% | 97.5% | 98.9% |

- 2,847 duplicate rows, all fraud; 86% of test frauds have a twin in training
- Median 10 fraud transactions per compromised card; 99% of test fraud cards also appear as fraud in training under a random split
- Honest result still beats the ABC Bank goal (≥ 80% of fraud by value), but the agent's evidence and claims were wrong
