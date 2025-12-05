import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_BASE_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def analyze_with_llm(resume_text, jd_text):
    prompt = f"""
You are an expert career advisor and hiring manager.
Evaluate the following resume against the given job description. Provide:
1. Fit Score (0 to 100).
2. Reasoning for the score.
3. Whether the candidate is a good fit (Yes/No).
4. Top strengths and key improvement areas.
5. A short hiring recommendation summary.

Resume:
{resume_text}

Job Description:
{jd_text}
"""

    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": "You are an expert in resume evaluation."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4
    }

    try:
        response = requests.post(GROQ_BASE_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as http_err:
        return f"LLM evaluation failed: {http_err}"
    except Exception as e:
        return f"LLM evaluation failed: {e}"
