import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = "https://api.openai.com/v1/chat/completions"
DEFAULT_MODEL = "gpt-4o-mini"


def _build_headers():
    if not OPENAI_API_KEY:
        raise ValueError(
            "OPENAI_API_KEY is not set. Please configure it before running the evaluator."
        )

    return {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
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
        "model": DEFAULT_MODEL,
        "messages": [
            {"role": "system", "content": "You are an expert in resume evaluation."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.4,
    }

    try:
        headers = _build_headers()
        response = requests.post(OPENAI_BASE_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as http_err:
        return f"LLM evaluation failed: {http_err}"
    except Exception as e:
        return f"LLM evaluation failed: {e}"
