# BUILD LOG – AI Phishing Detection Tool

## Engineering Objective

Build a SOC-style AI phishing detection system using structured LLM prompting, grounding data, and iterative prompt engineering.

---

# Build Timeline

## Phase 1 – System Initialization
- Designed FastAPI backend structure
- Created /analyze endpoint for email input
- Established basic frontend communication flow

---

## Phase 2 – Prompt Engineering Iteration

### Version 1 (Baseline)
- Freeform classification prompt
- Output inconsistent and unstructured

### Version 2 (SOC Role Introduction)
- Added SOC analyst role
- Introduced structured reasoning format

### Version 3 (Final System)
- Strict JSON schema enforcement
- Risk scoring (0–100)
- Added grounding files:
  - phishing_rules.json
  - examples.json

Outcome: Stable, structured, SOC-aligned outputs

---

## Phase 3 – System Integration
- Connected frontend (React) to FastAPI backend
- Integrated OpenAI API
- Ensured structured JSON parsing compatibility

---

## Phase 4 – Deployment Engineering
- Deployed backend on Render
- Deployed frontend on Vercel
- Fixed:
  - CORS issues
  - Vite production build errors
  - API routing mismatches

---

## Phase 5 – Evaluation Implementation
- Built held-out dataset (phishing, legitimate, edge cases)
- Measured:
  - accuracy
  - false positives
  - false negatives
- Validated SOC-style decision behavior

---

# Key Engineering Insight

System performance improved primarily through:
- structured output constraints
- grounding data injection
- iterative prompt refinement (V1 → V3)