# BUILD LOG – AI Phishing Detection Tool

## Project Goal
Build an AI-assisted phishing detection tool that helps users and SOC analysts identify phishing emails using structured AI analysis.

---

# Initial Idea

The project was inspired by the growing number of phishing attacks targeting students and organizations. As a cybersecurity graduate student, I wanted to build a practical AI tool that could analyze suspicious emails and explain phishing indicators in a structured way.

---

# Prompt Iteration History

## Prompt Version 1
Initial prompt asked the AI to classify emails as phishing or safe.

### Problems
- Responses were inconsistent
- Output formatting changed between requests
- Explanations were vague

---

## Prompt Version 2
Added SOC analyst role and structured JSON formatting.

### Changes
- Added:
  "You are a cybersecurity SOC analyst."
- Added strict JSON schema
- Added phishing indicators

### Improvements
- More consistent output
- Easier frontend parsing
- Better reasoning quality

---

## Prompt Version 3
Added grounding files using:
- phishing_rules.json
- examples.json

### Improvements
- Reduced hallucinations
- Better phishing detection accuracy
- More realistic explanations

---

# AI-Assisted Development Workflow

GitHub Copilot and ChatGPT were used throughout development to:

- troubleshoot deployment issues
- debug Vite asset path problems
- configure Render deployment
- improve FastAPI API structure
- refine prompt engineering
- improve JSON output consistency

The biggest lesson learned was that providing strong context and constraints to AI tools produces significantly better results than relying on repeated corrections afterward.

---

# Deployment Challenges

## Backend Deployment
### Problem
Render deployment failed because Python 3.14 caused pydantic-core build errors.

### Solution
Added:
runtime.txt

with:
python-3.11.9

---

## GitHub Secret Scanning
### Problem
GitHub blocked pushes due to exposed OpenAI API key in .env.

### Solution
- Removed .env from git history
- Added .env to .gitignore
- Used Render environment variables instead

---

## Frontend Deployment
### Problem
Vercel deployment returned blank pages and asset 404 errors.

### Cause
Incorrect Vite production asset paths.

### Solution
- Rebuilt deployment
- Corrected Vite configuration
- Reconfigured Vercel deployment

---

# Final Architecture

Frontend:
- React
- Vite
- Vercel

Backend:
- FastAPI
- Python
- Render

AI:
- OpenAI API

Grounding:
- phishing_rules.json
- examples.json

---

# Future Improvements

- Larger phishing dataset
- Better evaluation metrics
- URL reputation analysis
- Improved UI/UX
- Reduced backend cold-start latency