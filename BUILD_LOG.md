# BUILD LOG – AI Phishing Detection Tool

## Project Goal

Build an AI-assisted phishing detection system that helps users and SOC analysts identify phishing emails using structured AI analysis, grounded context, and measurable evaluation.

---

# System Overview

This project is an AI-powered phishing detection system designed for SOC-style email analysis.

The system:
- Accepts raw email input from a frontend interface
- Sends it to a FastAPI backend
- Uses an LLM with structured prompting and grounding data
- Returns:
  - classification (phishing / legitimate / suspicious)
  - risk score (0–100)
  - explanation of phishing indicators

---

# Initial Idea

The project was inspired by the growing number of phishing attacks targeting students and organizations. As a cybersecurity graduate student, I wanted to build a practical AI tool that simulates SOC analyst workflows and applies structured reasoning to email threat detection.

---

# Prompt Iteration History

## Prompt Version 1 (Baseline)

Initial prompt:
"Classify if the email is phishing or not."

### Problems
- Inconsistent responses
- No structured output
- Vague reasoning
- Difficult frontend parsing

**Impact:** Demonstrated need for structured constraints and role definition.

---

## Prompt Version 2 (SOC Analyst Framing)

Added SOC analyst role:
"You are a cybersecurity SOC analyst analyzing emails for phishing indicators."

Added:
- structured JSON output requirement
- phishing indicators list

### Improvements
- More consistent classification
- Improved reasoning quality
- Better integration with frontend

**Impact:** Introduced domain specialization and improved reliability.

---

## Prompt Version 3 (Production Version)

Final improvements:
- Strict JSON schema enforced
- Risk scoring (0–100) added
- Grounding files integrated:
  - phishing_rules.json
  - examples.json

### Improvements
- Reduced hallucinations
- Stable structured output
- Better phishing detection consistency
- Improved SOC realism

**Impact:** Production-ready prompt with grounded reasoning and structured output.

---

# Evaluation Integration

The final system was tested using a held-out dataset of phishing, legitimate, and edge-case emails.

Evaluation focused on:
- classification accuracy
- false positives (legitimate marked as phishing)
- false negatives (phishing marked as legitimate)
- risk score consistency

This ensured the model behaves as a measurable SOC-style detection system rather than a simple chatbot.

---

# AI-Assisted Development Workflow

AI tools (ChatGPT + GitHub Copilot) were used as development assistants, not autonomous builders.

They supported:
- debugging backend FastAPI routing issues
- resolving CORS and deployment errors
- fixing Vite production build and asset path issues
- refining structured JSON prompt design
- improving phishing classification consistency
- accelerating iteration of prompt versions

Key insight:
AI tools perform best when given strict constraints, structured output formats, and domain-specific context (SOC analyst role + grounding data).

---

# Deployment Challenges

## Backend Deployment (Render)

### Problem
Deployment failed due to Python version mismatch (Pydantic build errors).

### Solution
Pinned runtime:
runtime.txt → python-3.11.9

### Key Learning
Production environments require strict dependency and runtime version control.

---

## GitHub Secret Scanning

### Problem
Push blocked due to exposed OpenAI API key in .env.

### Solution
- Removed .env from Git history
- Added .env to .gitignore
- Migrated secrets to Render environment variables

### Key Learning
Proper secret management is critical in production AI systems.

---

## Frontend Deployment (Vercel)

### Problem
Blank page and 404 asset errors during deployment.

### Cause
Incorrect Vite production configuration.

### Solution
- Fixed Vite base path configuration
- Rebuilt production bundle
- Reconfigured Vercel deployment settings

### Key Learning
Frontend build tooling configuration is as important as backend logic.

---

# Final Architecture

Frontend (React + Vite on Vercel)
→ Captures email input and sends request to backend API

Backend (FastAPI on Render)
→ Processes request and constructs structured prompt

LLM Layer (OpenAI API)
→ Performs phishing classification using:
   - SOC analyst system prompt
   - phishing_rules.json (grounding)
   - examples.json (few-shot learning)

Output Layer
→ Returns structured JSON:
   - classification
   - risk score
   - phishing indicators explanation

---

# Engineering Summary

This project demonstrates an end-to-end AI security system combining:

- prompt engineering lifecycle (V1 → V3)
- grounded few-shot learning
- structured evaluation methodology
- full-stack deployment pipeline
- SOC-style threat analysis modeling

The goal was not only to build a working tool, but to design a measurable, reproducible AI pipeline for phishing detection.

---

# Future Improvements

- Expand phishing dataset for evaluation
- Improve false positive reduction
- Add email header and domain analysis
- Integrate external threat intelligence APIs
- Reduce backend cold-start latency
- Improve UI/UX experience