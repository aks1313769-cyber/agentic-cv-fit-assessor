import streamlit as st
st.set_page_config(page_title="LLM Resume Analyzer", layout="centered")
from resume_parse import extract_text_from_pdf
from skill_extract import  get_resume_details,compare_resume_with_jd,get_final_score_and_suggestions
from llm import analyze_with_llm

st.title("LLM Resume Analyzer")
st.caption("Powered by modern LLMs for skill extraction, similarity scoring, and intelligent feedback.")

upload_option = st.radio("Choose Resume Input Method:", ["Upload PDF", "Paste Text"])
resume_text = ""
if upload_option == "Upload PDF":
    resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    if resume_file:
        resume_text = extract_text_from_pdf(resume_file)
        # resume_text = extract_text_from_pdf(resume_file.name)

elif upload_option == "Paste Text":
    resume_text = st.text_area("Paste your Resume Text", height=300)

jd_input = st.text_area("Paste the Job Description", height=250)

if st.button("Analyze"):
    if not resume_text.strip() or not jd_input.strip():
        st.error("Please upload a resume and paste a job description.")
    else:
        with st.spinner("Analyzing Resume with Agentic Intelligence..."):
            resume_details = get_resume_details(resume_text)
            analysis = compare_resume_with_jd(resume_details, jd_input)
            score, keyword_match = get_final_score_and_suggestions(analysis)
            llm_insight = analyze_with_llm(resume_text, jd_input)

        st.markdown("---")
        st.subheader("Analysis Results")
        st.metric("Skill Similarity Score", f"{score}%")
        st.metric("JD Keyword Match", f"{keyword_match}%")

        # st.markdown("### 🛠 Skills Overview")
        st.write(f"**Matched Skills**: {', '.join(analysis['matched_skills']) or 'None'}")
        st.write(f"**Missing Skills**: {', '.join(analysis['missing_skills']) or 'None'}")

        st.markdown("###LLM-Based Feedback")
        st.write(llm_insight)