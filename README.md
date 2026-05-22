# AI Phishing Detection Backend

Backend API for the AI-powered phishing detection system.

# System Architecture

Frontend (React + Vite on Vercel)
        ↓
Backend API (FastAPI on Render)
        ↓
OpenAI API
        ↓
Structured JSON phishing analysis
        ↓
Risk score + phishing indicators

## Features

- FastAPI backend
- OpenAI-powered phishing analysis
- Structured JSON responses
- Few-shot grounding
- SOC analyst prompt engineering
- Rule-based phishing indicators

---

# Tech Stack

- Python
- FastAPI
- OpenAI API
- Render deployment

---
# Security Considerations

- API keys stored in environment variables
- No user email persistence
- CORS restricted to frontend domain
- Structured JSON outputs for reliable parsing
- Backend input validation implemented
---

# API Endpoint

## POST /analyze

Analyzes suspicious email content and returns phishing risk analysis.

Example request:

```json
{
  "message": "Your bank account has been locked. Click here immediately."
}
# Prompt Engineering Strategy

The system prompt evolved through multiple iterations:

- Initial freeform classification
- Structured SOC analyst role assignment
- Strict JSON schema enforcement
- Few-shot grounding using phishing_rules.json and examples.json

The final prompt was optimized for:
- consistent formatting
- reduced hallucinations
- explainable phishing analysis