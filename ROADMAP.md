# Project Roadmap – AI Phishing Detection System

---

# Problem Statement

Phishing attacks remain one of the most common cybersecurity threats targeting students, employees, and organizations. These attacks rely on social engineering techniques such as urgency, impersonation, and credential theft, making them difficult for non-experts to detect.

This project addresses the need for an AI-assisted phishing detection system that can analyze emails, identify malicious patterns, and explain security risks in a structured and interpretable format.

---

# Project Goal

Build a full-stack AI-powered phishing detection system capable of:

- analyzing raw email content
- identifying phishing indicators using LLM reasoning
- producing structured JSON security reports
- providing explainable risk scoring (0–100)
- simulating SOC analyst decision-making workflows

---

# Success Criteria (Measurable Outcomes)

The system is considered successful if it achieves:

- ≥ 90% classification accuracy on evaluation dataset
- structured JSON output consistency (100% parseable responses)
- correct identification of phishing vs legitimate emails
- explainable reasoning for all predictions
- successful full-stack deployment (frontend + backend)
- stable API communication between services

---

# System Architecture

Frontend (React + Vite on Vercel)  
→ captures email input from user interface  

Backend (FastAPI on Render)  
→ processes request and constructs structured prompt  

LLM Layer (OpenAI API)  
→ performs phishing classification using:
  - SOC analyst system prompt
  - phishing_rules.json (grounding data)
  - examples.json (few-shot learning)

Output Layer  
→ returns structured JSON response:
  - classification (phishing / legitimate / suspicious)
  - risk score (0–100)
  - phishing indicators explanation

---

# Tech Stack

## Frontend
- React
- Vite

## Backend
- FastAPI
- Python

## AI Layer
- OpenAI API

## Deployment
- Vercel (Frontend)
- Render (Backend)

---

# Development Strategy (Iterative Engineering Process)

The system was developed using an iterative full-stack and prompt engineering approach:

## Phase 1 – UI Foundation
- Built React frontend interface
- Designed email input workflow
- Established API communication structure

## Phase 2 – Backend Development
- Created FastAPI server
- Implemented /analyze endpoint
- Structured request/response schema

## Phase 3 – AI Integration
- Integrated OpenAI API
- Designed SOC analyst system prompt
- Introduced structured JSON output format

## Phase 4 – Prompt Engineering Iteration
- Version 1: basic classification (unstructured output)
- Version 2: SOC analyst role added
- Version 3: strict JSON schema + risk scoring + grounding data

## Phase 5 – Grounding & Reliability Improvements
- Added phishing_rules.json (security heuristics)
- Added examples.json (few-shot learning dataset)
- Reduced hallucination and improved consistency

## Phase 6 – Deployment
- Deployed backend on Render
- Deployed frontend on Vercel
- Configured environment variables and CORS
- Fixed production build issues (Vite configuration)

## Phase 7 – Evaluation
- Tested system using held-out dataset
- Measured accuracy, false positives, and false negatives
- Validated SOC-style decision behavior

---

# Evaluation Alignment

The roadmap directly aligns with evaluation outputs:

- prompt iteration → improved accuracy
- grounding → reduced hallucinations
- structured JSON → improved reliability
- deployment → real-world system validation

This ensures the project is not only functional but measurable and reproducible.

---

# Key Engineering Decisions

- Enforced structured JSON output for machine reliability
- Used SOC analyst role to improve reasoning quality
- Introduced grounding files to reduce hallucination
- Designed stateless backend for scalability
- Separated frontend and backend for modular architecture

---

# Future Improvements

- Expand evaluation dataset size and diversity
- Add email header + domain reputation analysis
- Integrate external threat intelligence APIs
- Improve classification of edge-case phishing simulations
- Reduce backend cold-start latency
- Enhance UI/UX for SOC analyst workflows

---