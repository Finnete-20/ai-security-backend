# AI Phishing Detection Backend

## Overview

Backend API for SOC-style AI phishing detection using OpenAI.

---

# System Architecture
The architecture below describes the current implementation of the AI-powered phishing detection pipeline. The system uses structured prompting, grounding files, and SOC-style reasoning to analyze email content and return explainable JSON security reports.

```text
┌────────────────────┐
│  User Email Input  │
│  (Frontend UI)     │
└────────────────────┘
            │
            ▼
┌────────────────────┐
│ React + Vite       │
│ Frontend (Vercel)  │
└────────────────────┘
            │
            ▼
┌──────────────────────────┐
│ FastAPI Backend (Render) │
│ /analyze endpoint        │
└──────────────────────────┘
            │
            ▼
┌──────────────────────────┐
│ Prompt Construction      │
│ - SOC analyst role       │
│ - JSON schema rules      │
│ - Risk scoring logic     │
└──────────────────────────┘
            │
            ▼
┌──────────────────────────┐
│ Grounding Layer          │
│ - phishing_rules.json    │
│ - examples.json          │
└──────────────────────────┘
            │
            ▼
┌──────────────────────────┐
│ OpenAI API Classification│
│ Structured phishing      │
│ analysis + reasoning     │
└──────────────────────────┘
            │
            ▼
┌──────────────────────────┐
│ Structured JSON Response │
│ classification           │
│ risk_score               │
│ indicators               │
│ explanation              │
└──────────────────────────┘
            │
            ▼
┌────────────────────┐
│ Frontend Display   │
│ Risk visualization │
│ SOC-style output   │
└────────────────────┘
```

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
## Repository Structure

### Frontend Repository

```text
/frontend
├── src/                       # React frontend source code
├── public/                    # Static frontend assets
├── screenshots/               # UI screenshots and previews
├── BUILD_LOG.md               # Frontend engineering and deployment history
├── EVALUATION.md              # Frontend-linked evaluation documentation
├── ROADMAP.md                 # Planned system improvements
├── examples.json              # Frontend testing/example inputs
├── vite.config.js             # Vite configuration
├── package.json               # Frontend dependencies and scripts
├── index.html                 # Frontend HTML entry point

 
 ### Backend Repository
/backend
├── main.py                     # FastAPI backend entry point
├── phishing_rules.json         # Grounding rules for phishing detection
├── examples.json               # Few-shot grounding examples
├── BUILD_LOG.md                # Engineering and deployment history
├── evaluation.md               # Evaluation methodology and metrics
├── requirements.txt            # Backend dependencies
├── runtime.txt                 # Deployment runtime configuration
│
├── /evaluation
│   ├── phishing_samples.json  # Held-out phishing dataset
│   ├── legit_samples.json     # Legitimate email dataset
│   ├── edge_cases.json        # Ambiguous and edge-case emails
│   └── evaluation_results.md  # Detailed evaluation outputs

# Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
---

# Tech Stack

- FastAPI
- Python
- OpenAI API
- Render + Vercel
```