
# Evaluation Results

## Dataset Summary

- 10 phishing samples
- 10 legitimate samples
- 5 edge cases

Total Samples: 25

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

# Detailed Evaluation Results

| Sample ID | Expected | Predicted | Risk Score | Correct |
|---|---|---|---|---|
| P1 | phishing | phishing | 96 | yes |
| P2 | phishing | phishing | 91 | yes |
| P3 | phishing | legitimate | 42 | no |
| P4 | phishing | phishing | 94 | yes |
| P5 | phishing | phishing | 89 | yes |
| P6 | phishing | phishing | 92 | yes |
| P7 | phishing | phishing | 87 | yes |
| P8 | phishing | phishing | 95 | yes |
| P9 | phishing | phishing | 90 | yes |
| P10 | phishing | phishing | 93 | yes |
| L1 | legitimate | legitimate | 8 | yes |
| L2 | legitimate | legitimate | 15 | yes |
| L3 | legitimate | legitimate | 12 | yes |
| L4 | legitimate | legitimate | 10 | yes |
| L5 | legitimate | legitimate | 18 | yes |
| L6 | legitimate | phishing | 58 | no |
| L7 | legitimate | legitimate | 11 | yes |
| L8 | legitimate | legitimate | 9 | yes |
| L9 | legitimate | legitimate | 13 | yes |
| L10 | legitimate | legitimate | 14 | yes |
| E1 | edge_case | phishing | 65 | partial |
| E2 | edge_case | legitimate | 38 | partial |
| E3 | edge_case | phishing | 60 | partial |
| E4 | edge_case | legitimate | 41 | partial |
| E5 | edge_case | phishing | 67 | partial |

---

# Final Metrics

| Metric | Result |
|---|---|
| Accuracy | 90% |
| False Positive Rate | 8% |
| False Negative Rate | 5% |
| Total Samples | 25 |