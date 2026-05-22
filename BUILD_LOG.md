# BUILD LOG – AI Phishing Detection Tool

## Project Goal

Build an AI-assisted phishing detection system that helps users and SOC analysts identify phishing emails using structured AI analysis, grounded context, and measurable evaluation.

The system is designed as a prototype SOC (Security Operations Center) tool that applies LLM-based reasoning to email threat classification.

---

# System Overview (End-to-End Architecture)

This project implements a full-stack AI phishing detection pipeline:

Frontend (React + Vite on Vercel)
→ Captures raw email input and sends request to backend API

Backend (FastAPI on Render)
→ Preprocesses request and constructs structured LLM prompt

LLM Layer (OpenAI API)
→ Performs phishing classification using:
  - SOC analyst system prompt
  - phishing_rules.json (grounded security rules)
  - examples.json (few-shot learning examples)

Output Layer
→ Returns structured JSON response:
  - classification (phishing / legitimate / suspicious)
  - risk score (0–100)
  - phishing indicators explanation

---

# Initial Idea

The project was inspired by the increasing frequency and sophistication of phishing attacks targeting students, universities, and enterprise environments.

As a cybersecurity graduate student, the goal was to build a practical SOC-style AI assistant that mimics real-world email triage workflows using structured reasoning and measurable outputs.

---

# Prompt Engineering Iteration History (Core Contribution)

This project demonstrates iterative prompt engineering with measurable system improvement.

## Prompt Version 1 (Baseline – Unstructured)

Initial prompt:
"Classify if the email is phishing or not."

### Limitations
- Inconsistent outputs
- No structured JSON format
- Weak reasoning transparency
- Difficult frontend integration

### Outcome
Established baseline and highlighted need for structured constraints.

---

## Prompt Version 2 (SOC Analyst Framing)

Added SOC analyst role:
"You are a cybersecurity SOC analyst analyzing emails for phishing indicators."

Added:
- structured JSON output format
- phishing indicators field

### Improvements
- Increased classification consistency
- Improved reasoning quality
- Better integration with frontend parsing

### Outcome
Introduced domain-specific reasoning behavior aligned with SOC workflows.

---

## Prompt Version 3 (Production Version – Final System)

Final improvements:
- Strict JSON schema enforcement
- Risk scoring system (0–100)
- Integration of grounding datasets:
  - phishing_rules.json
  - examples.json

### Improvements
- Significant reduction in hallucinated outputs
- Stable structured JSON responses
- Improved phishing detection consistency
- Better SOC realism in reasoning process

### Outcome
Final production-ready prompt with grounded reasoning + structured outputs.

---

# Evaluation Integration (Measured System Design)

The final system was evaluated using a held-out dataset of phishing, legitimate, and edge-case emails.

Evaluation metrics included:
- classification accuracy
- false positives (legitimate classified as phishing)
- false negatives (phishing classified as legitimate)
- risk score consistency across samples

## Key Insight

This evaluation demonstrates that system performance is directly influenced by:
- prompt structure
- grounding quality
- few-shot example design

This transforms the system from a chatbot into a measurable SOC-style detection pipeline.

---

# AI-Assisted Development Workflow

AI tools (ChatGPT + GitHub Copilot) were used as development accelerators, not autonomous builders.

They supported:
- debugging FastAPI backend routing issues
- resolving CORS and API integration problems
- fixing Vite production build and deployment errors
- refining structured JSON prompt design
- improving phishing classification consistency
- accelerating iteration of prompt versions

## Key Engineering Insight

Performance improved significantly when:
- strict output schemas were enforced
- domain context (SOC analyst role) was added
- grounding data was introduced

This confirms that LLM performance is highly dependent on structured constraints and contextual grounding.

---

# Deployment Challenges & Resolutions

## Backend Deployment (Render)

### Issue
Deployment failure due to Python version mismatch (Pydantic build errors).

### Fix
Pinned runtime using:
runtime.txt → python-3.11.9

### Learning
Production AI systems require strict dependency and runtime control.

---

## GitHub Secret Exposure Protection

### Issue
Push blocked due to exposed API key in .env file.

### Fix
- Removed .env from Git history
- Added .env to .gitignore
- Migrated secrets to Render environment variables

### Learning
Secure secret management is essential in production AI systems.

---

## Frontend Deployment (Vercel)

### Issue
Blank page and asset 404 errors.

### Root Cause
Incorrect Vite production build configuration.

### Fix
- Fixed Vite base path configuration
- Rebuilt production bundle
- Reconfigured Vercel deployment settings

### Learning
Frontend build configuration is critical in full-stack AI deployment pipelines.

---

# Engineering Summary

This project demonstrates a complete AI security system combining:

- iterative prompt engineering (V1 → V3)
- grounded few-shot learning
- structured evaluation methodology
- full-stack deployment (Vercel + Render)
- SOC-style threat analysis modeling

The system was designed not only as a functional tool, but as a **measurable and reproducible AI pipeline for phishing detection**.

---

# Future Improvements

- Expand evaluation dataset for higher statistical reliability
- Improve false positive reduction in edge cases
- Add email header + domain reputation analysis
- Integrate external threat intelligence APIs
- Reduce backend cold-start latency
- Improve UI/UX for SOC analyst workflow simulation