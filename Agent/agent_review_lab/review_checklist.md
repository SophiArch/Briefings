# Reviewing an Agent's Data Science Work — Checklist

Review the agent's notebook as you would a junior colleague's pull request.
For each item, write **OK**, **Problem** (with evidence), or **Not checked**.

## 1. Reproduce
- [ ] The notebook runs top to bottom on a fresh kernel
- [ ] I get the same headline number the agent reported

## 2. Data
- [ ] Duplicates were checked **before** any ID column was dropped
- [ ] Class balance is natural, not manufactured (oversampling, copied rows)
- [ ] Every dropped column and row has a stated reason
- [ ] No feature leaks the label or information from after the transaction

## 3. Split
- [ ] No identical or near-identical rows on both sides of the split
- [ ] Related rows (same customer, same card, same day) stay on one side when production would see them as new
- [ ] Preprocessing (scaling, encoding, resampling) is fitted on training data only

## 4. Metrics
- [ ] A majority-class baseline is reported
- [ ] The headline metric matches the business goal (here: recall by **value** ≥ 80%)
- [ ] Precision or alert volume is reported (analyst workload)
- [ ] Results are on a held-out test set, not the data used for tuning

## 5. Claims
- [ ] Every claim in the summary is backed by an output in the notebook
- [ ] Words like "production-ready", "highly accurate" or "robust" have evidence or are removed
- [ ] Limitations and risks are stated

## 6. Verdict
- [ ] **Approve** — numbers are trustworthy and claims match evidence
- [ ] **Request changes** — list what must be fixed
- [ ] **Reject** — the approach is wrong; rewrite the brief

> Agents fail quietly: the code runs, the plots look fine, and the summary is confident.
> Your review is the only thing between a wrong number and a business decision.
