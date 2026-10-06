# Brief v1 — the one-liner

Paste this into your coding agent (Claude Code, GitHub Copilot agent mode, Gemini in Colab, Copilot in Fabric notebooks, …)
together with the dataset URL:

```text
Build a fraud detection model on fraud_dataset.csv and tell me how accurate it is.

Dataset: https://raw.githubusercontent.com/JasonL888/AI_Experiments/refs/heads/main/Datasets/fraud_dataset.csv
```

## Why this brief is weak

- **Asks for the wrong metric.** "How accurate" invites accuracy, the metric that hides problems on imbalanced data
- **No business goal.** The agent can't know the bank cares about fraud caught *by value*, or about analyst workload
- **No standard of evidence.** Nothing says "prove the test set is clean" or "compare against a baseline"
- **No definition of done.** So the agent decides for itself, and it usually decides "ready for production"
