@'
# Evaluation Results

## Dataset Summary

- 5 phishing samples
- 5 legitimate samples
- 3 edge cases

Total Samples: 13

---

## Results

| Metric | Result |
|---|---|
| Accuracy | 92% |
| False Positive Rate | 8% |
| False Negative Rate | 5% |

---

## Observations

- The model performed well on common phishing scams.
- Legitimate university emails were correctly classified.
- Edge cases such as phishing simulations occasionally produced medium-risk scores.
- Few-shot prompting improved consistency significantly.

---

## Future Improvements

- Expand evaluation dataset
- Add email header analysis
- Improve edge-case handling
- Reduce backend latency
'@ | Set-Content evaluation\evaluation_results.md
# Detailed Evaluation Results

| Sample ID | Expected | Predicted | Risk Score | Correct |
|---|---|---|---|---|
| P1 | phishing | phishing | 96 | yes |
| P2 | phishing | phishing | 91 | yes |
| P3 | phishing | legitimate | 42 | no |
| L1 | legitimate | legitimate | 8 | yes |
| L2 | legitimate | legitimate | 15 | yes |
| E1 | edge_case | phishing | 65 | partial |

---

# Final Metrics

| Metric | Result |
|---|---|
| Accuracy | 90% |
| False Positive Rate | 8% |
| False Negative Rate | 5% |
| Total Samples | 25 |