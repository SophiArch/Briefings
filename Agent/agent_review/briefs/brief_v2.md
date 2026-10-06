# Brief v2 — a brief written like a spec

A good brief states the **goal, constraints and standard of evidence**. It does not hand the agent the answers:
note that it never mentions duplicates or card-level leakage by name.

```text
## Context
You are helping a retail bank's Security/Fraud team. Today fraud is assessed by analysts reading
transaction rows one at a time. Dataset (one row per card transaction, label = is_fraud):
https://raw.githubusercontent.com/JasonL888/AI_Experiments/refs/heads/main/Datasets/fraud_dataset.csv

## Goal
Build a model that flags fraudulent transactions. The business target is:
flag at least 80% of confirmed fraud BY DOLLAR VALUE, while keeping false alerts low enough
for analysts to review (report precision).

## Before modelling
- Profile the data and report anything that could make evaluation misleading
  (duplicates, ID columns, class balance, columns that leak the label or the future).
- Do not drop columns or rows until you have explained why, with evidence.

## Evaluation rules
- The test set must mirror production: the model will score transactions from cards
  it has never seen. Choose and justify a split that reflects this.
- Report a majority-class baseline next to every metric.
- Report recall by count, recall by dollar value, and precision. Accuracy is secondary.
- If a result looks too good, investigate before reporting it.

## Deliverables
1. A notebook that runs top to bottom.
2. A short summary: headline numbers, what you checked, what you changed and why,
   and remaining risks. Do not claim the model is production-ready.

## Working style
Stop and ask me if the data contradicts this brief, or if you need to make an assumption
that changes the result by more than a few percentage points.
```

## What changed from v1

| v1 gap | v2 fix |
|--------|--------|
| Wrong metric ("accurate") | Business metric stated: recall by value ≥ 80%, plus precision |
| No context | Who the user is and how fraud is handled today |
| Silent data changes | "Explain before you drop", "report what could mislead" |
| Unrealistic test set | Split must mirror production (unseen cards) |
| No baseline | Baseline required next to every metric |
| Agent decides "done" | Deliverables listed; production-ready claim forbidden |
| No escalation | When to stop and ask |
