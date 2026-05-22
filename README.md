# AI Phishing Detection Backend

Backend API for the AI-powered phishing detection system.

---

# System Architecture

Frontend (React + Vite on Vercel)  
→ Backend API (FastAPI on Render)  
→ OpenAI API (LLM inference layer)  
→ Structured JSON phishing analysis  
→ Risk score + phishing indicators output  

---

# Features

- FastAPI backend for phishing detection
- OpenAI-powered email classification
- SOC analyst structured prompt engineering
- Strict JSON schema enforcement
- Few-shot grounding (phishing_rules.json + examples.json)
- Risk scoring (0–100)
- Explainable phishing indicators
- Stateless API design (no email storage)

---

# Tech Stack

- Python
- FastAPI
- OpenAI API
- Render (deployment)
- Vercel (frontend)

---

# API Endpoint

## POST `/analyze`

Analyzes email content and returns phishing risk assessment.

---

## Request

```json
{
  "message": "Your bank account has been locked. Click here immediately."
}
```

---

## Response

```json
{
  "classification": "phishing",
  "risk_score": 96,
  "indicators": [
    "Urgent language",
    "Credential solicitation",
    "Suspicious link behavior"
  ],
  "explanation": "The email contains classic phishing patterns including urgency and request for user credentials."
}
```

---

# Security Considerations

- API keys stored in environment variables
- No persistence of user email data
- CORS restricted to frontend domain
- Input validation enforced at API level
- Structured JSON output prevents injection ambiguity

---

# Prompt Engineering Strategy

The system prompt evolved through iterative development:

## Version 1
- Freeform classification only
- No structure
- Inconsistent outputs

## Version 2
- SOC analyst role added
- Structured reasoning introduced
- Improved consistency

## Version 3 (Final)
- Strict JSON schema enforced
- Risk scoring system added
- Few-shot grounding via:
  - phishing_rules.json
  - examples.json

### Final Optimization Goals
- High consistency across responses
- Reduced hallucination rate
- SOC-style explainability
- Machine-parseable outputs

---

# Evaluation Summary

The system was evaluated using a controlled dataset of phishing, legitimate, and edge-case emails.

Key metrics:
- Accuracy: ~90–92%
- False positives: ~8%
- False negatives: ~5%

Evaluation demonstrates strong performance on clear phishing cases and expected degradation on ambiguous edge cases.

---

# How to Run Locally

## Backend setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Environment variables

```bash
OPENAI_API_KEY=your_key_here
```

---

# Future Improvements

- Expand phishing dataset coverage
- Add email header + domain analysis
- Integrate threat intelligence APIs
- Improve edge-case classification
- Reduce backend cold-start latency
- Enhance UI/UX for SOC workflows