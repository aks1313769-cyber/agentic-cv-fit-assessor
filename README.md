# 🤖 LLM Resume Analyzer

A professional-grade resume-job fit assessment tool using LLMs and skill intelligence.

## 🚀 Overview

This app allows you to:
- Upload a resume (PDF or raw text)
- Paste any job description (JD)
- Automatically extract relevant skills
- Evaluate resume-JD alignment
- Get detailed feedback via LLM (Mixtral via Groq)

> Useful for applicants, recruiters, and hiring managers seeking skill-based alignment.

## 🧠 Powered by:
- `sentence-transformers/all-MiniLM-L6-v2` (skill embedding)
- `Mixtral-8x7b` via `Groq API` (LLM feedback)
- Streamlit UI (interactive, fast)

## 📁 File Structure

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit app |
| `resume_parse.py` | Extracts text from PDF resumes |
| `skill_extract.py` | Tokenizes, matches, scores skills |
| `llm.py` | Sends resume & JD to Mixtral API |
| `prompt.py` | Stores LLM prompt template |
| `skills.json` | Domain-specific skill bank |
| `text_clean.py` | NLP cleanup using spaCy |
| `requirements.txt` | All dependencies listed here |

---
##🔐 Privacy Notes
No data is stored. All processing happens in memory and is user-side unless deployed to a server.

git clone https://github.com/aks1313769-cyber/agentic-cv-fit-assessor.git
cd agentic-cv-fit-assessor
