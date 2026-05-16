from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Phishing Detection API is running"}

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class InputData(BaseModel):
    message: str

# Load optional data
try:
    with open("phishing_rules.json", "r") as f:
        rules = json.load(f)
except:
    rules = {}

try:
    with open("examples.json", "r") as f:
        examples = json.load(f)
except:
    examples = {}

SYSTEM_PROMPT = """
You are a SOC cybersecurity phishing detection analyst.

Return ONLY valid JSON:

{
  "risk_score": 1-10,
  "attack_type": "string",
  "phishing_indicators": ["string"],
  "social_engineering_tactics": ["string"],
  "recommended_action": "string"
}
"""

@app.post("/analyze")
def analyze(data: InputData):

    context = f"""
PHISHING RULES:
{json.dumps(rules)}

EXAMPLES:
{json.dumps(examples)}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "system", "content": context},
                {"role": "user", "content": data.message}
            ]
        )

        result = response.choices[0].message.content

        # 🔥 ALWAYS PARSE JSON
        parsed = json.loads(result)

        return {
            "status": "success",
            "analysis": parsed
        }

    except json.JSONDecodeError:
        return {
            "status": "error",
            "message": "Model returned invalid JSON",
            "raw_output": result
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }