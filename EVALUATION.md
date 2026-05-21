# Evaluation Report

## Goal
Evaluate the phishing detection accuracy of the AI-powered phishing detector.

---

# Test Dataset

The evaluation set included:

| Type | Count |
|---|---|
| Phishing Emails | 10 |
| Legitimate Emails | 10 |
| Edge Cases | 5 |

Examples included:
- phishing login scams
- fake password reset emails
- legitimate university emails
- promotional emails
- simulated phishing awareness emails

---

# Evaluation Criteria

The system was evaluated on:

1. Classification Accuracy
2. False Positive Rate
3. False Negative Rate
4. JSON Formatting Consistency
5. Explanation Quality

---

# Results

| Metric | Result |
|---|---|
| Total Emails Tested | 25 |
| Correctly Classified | 22 |
| Accuracy | 88% |
| False Positives | 2 |
| False Negatives | 1 |
| JSON Formatting Success | 100% |

---

# Strengths

- Correctly identified urgency language
- Detected suspicious links
- Produced consistent structured JSON output
- Generated understandable phishing explanations

---

# Weaknesses

- Some legitimate urgent emails were flagged as suspicious
- Marketing emails occasionally triggered phishing indicators

---

# Edge Case Example

## Email
"Your university password expires today. Reset immediately."

## Expected Result
Legitimate

## Actual Result
Suspicious

## Analysis
The urgency wording resembled phishing patterns even though the email was legitimate.

---

# Conclusion

The phishing detector performed well overall and demonstrated reliable structured phishing analysis. The largest improvement area is reducing false positives for legitimate urgent institutional emails.