cv_prompt_template = """
You are an expert recruiter. Given the following CV and Job Description (JD), assess the candidate's fit for the role.

CV:
{cv}

Job Description:
{jd}

Provide:
1. A short summary of match/mismatch
2. A rating out of 10
3. Suggestions to improve alignment
"""
