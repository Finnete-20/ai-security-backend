# AI Phishing Detection Backend

## Overview

Backend API for SOC-style AI phishing detection using OpenAI.

---

# System Architecture

Frontend (Vercel)
→ FastAPI Backend (Render)
→ OpenAI API
→ Structured JSON response

---

# Features

- Phishing email classification
- Risk scoring (0–100)
- SOC analyst reasoning format
- Structured JSON output
- Grounded prompting (rules + examples)

---

# API Endpoint

## POST /analyze

### Request
```json
{
  "message": "Your account will be locked. Click here immediately."
}
```

---

### Response
```json
{
  "classification": "phishing",
  "risk_score": 96,
  "indicators": [
    "Urgency",
    "Credential request",
    "Suspicious link pattern"
  ],
  "explanation": "Classic phishing pattern detected with urgency and credential harvesting intent."
}
```

---

# Security

- Environment-based API key storage
- No data persistence
- Input validation enforced
- CORS restricted

---

# Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
## Evaluation

See full system evaluation here: https://github.com/Finnete-20/ai-security-backend/blob/main/evaluation.md?utm_source=chatgpt.com


---

# Tech Stack

- FastAPI
- Python
- OpenAI API
- Render + Vercel
```