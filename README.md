# AI Phishing Detection Backend

Backend API for the AI-powered phishing detection system.

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