# 🤖 LLM Resume Analyzer

A professional-grade resume-job fit assessment tool using LLMs and skill intelligence.

## 🚀 Overview

This app allows you to:
- Upload a resume (PDF or raw text)
- Paste any job description (JD)
- Automatically extract relevant skills
- Evaluate resume-JD alignment
- Get detailed feedback via LLM (OpenAI ChatGPT)

> Useful for applicants, recruiters, and hiring managers seeking skill-based alignment.

## 🔑 Environment setup

Create a `.env` file (or export environment variables) with your OpenAI credentials:

```
OPENAI_API_KEY=your_api_key_here
```

You can copy `.env.example` to `.env` and fill in your key. The app uses the `gpt-4o-mini` Chat Completions model via the OpenAI API.

## 🧭 Quickstart (local)

1) **Clone** the repo (or open it in VS Code if already connected):

```bash
git clone https://github.com/aks1313769-cyber/agentic-cv-fit-assessor.git
cd agentic-cv-fit-assessor
```

2) **Create a virtual environment** (recommended) and activate it:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
```

3) **Install dependencies**:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4) **Set your OpenAI key** by creating `.env` (or exporting the variable) with `OPENAI_API_KEY`.

5) **Run the Streamlit app**:

```bash
streamlit run app.py
```

6) Open the printed URL (e.g., `http://localhost:8501`) in your browser. Upload a resume (PDF or text), paste a job description, and review the LLM feedback.

## 🧠 Powered by:
- `sentence-transformers/all-MiniLM-L6-v2` (skill embedding)
- `gpt-4o-mini` via `OpenAI API` (LLM feedback)
- Streamlit UI (interactive, fast)

## 📁 File Structure

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit app |
| `resume_parse.py` | Extracts text from PDF resumes |
| `skill_extract.py` | Tokenizes, matches, scores skills |
| `llm.py` | Sends resume & JD to OpenAI Chat Completions API |
| `prompt.py` | Stores LLM prompt template |
| `skills.json` | Domain-specific skill bank |
| `text_clean.py` | NLP cleanup using spaCy |
| `requirements.txt` | All dependencies listed here |

---
🔐 Privacy Notes
No data is stored. All processing happens in memory and is user-side unless deployed to a server.
