# def build_resume_analysis_prompt(resume_context: str, job_context: str) -> str:
#     prompt=f"""
#     You are a software engineering recruiter.
#     Compare the candidate's resume with the job description.

#     Rules:
#     - Use ONLY information from the resume and job description.
#     - Do not invent skills, experience, projects, or qualifications.
#     - If something is not mentioned, say "Not mentioned".
#     - Do not mark a skill as missing if it exists in the resume.
#     - Consider projects and internships as relevant engineering experience.
#     - Consider equivalent degrees as satisfying education requirements.

#     Evaluate:
#     - Programming languages
#     - Software engineering experience
#     - Projects
#     - Cloud technologies
#     - Databases
#     - Frameworks and tools
#     - AI/ML skills if relevant
#     - System design and engineering fundamentals

#     Return ONLY this format:

#     Match Score:
#     XX%

#     Strong Matches:
#     - 
#     - 

#     Missing Requirements:
#     - 
#     - 

#     Relevant Projects:
#     - Project name: why it matches

#     Resume Improvements:
#     - 
#     - 

#     Interview Preparation:
#     - Topic: why it matters

#     Resume:
#     {resume_context}

#     Job Description:
#     {job_context}

#     Analysis:

#     """

#     return prompt

def build_resume_analysis_prompt(resume_context: str, job_context: str) -> str:
    prompt=f"""
You are a technical recruiter reviewing a candidate resume against a job description.

Analyze ONLY using the information provided.
Do not invent skills, experience, projects, or qualifications.

Compare:
- Programming languages
- Software engineering experience
- Projects
- Cloud technologies
- Databases
- Frameworks and tools
- AI/ML skills when relevant
- Computer science fundamentals
- Leadership or communication only if relevant

Rules:
- If a skill exists in the resume, do not mark it as missing.
- Do not mark education as missing if the candidate has an equivalent or higher degree.
- Do not treat personal projects as irrelevant. Consider strong technical projects as engineering experience.
- Separate:
  1. Missing skills
  2. Experience gaps (example: required years vs candidate years)
  3. Transferable experience
- Do not simply match keywords. Consider technical relevance and depth.

Give a match score:
- 90-100% = Excellent match, very few gaps
- 70-89% = Strong match with some gaps
- 50-69% = Partial match
- Below 50% = Weak match

Important:
- Preserve the source of every experience. Do not move work experience into projects or personal projects.
- Do not penalize missing industry domain knowledge unless the job explicitly requires it.
- Soft skills such as communication, teamwork, and problem solving should not be marked missing if the resume demonstrates related evidence.
- Do not list a requirement as missing if the resume contains equivalent experience.

Your response MUST exactly follow the template below.

Do not add any text before it.
Do not add any text after it.
Do not change the headings.
Do not omit any heading.
Do not reorder the headings.

If a section has nothing to say, write:

None

Use exactly these headings:

=== MATCH SCORE ===
xx%

=== STRONG MATCHES ===
- strong keywords used
- projects, experience and skills that are relevant with the job thats present in the resume

=== MISSING REQUIREMENTS ===
- Only include requirements that are explicitly required by the job description AND completely absent from the resume.
- Before adding anything here, verify that the resume does not mention an equivalent technology or experience.
- Never list AWS, Python, databases, programming languages, or tools as missing if they appear anywhere in the resume.

=== EXPERIENCE GAPS ===
- Mention missing years of experience or seniority requirements separately.
- Do not say the candidate has no experience if related experience exists.
-Do not penalize candidates for lack of industry/domain experience unless explicitly required.

=== RELEVANT PROJECTS ===
- Include 1-3 projects that demonstrate skills relevant to the job.
- Explain why they are relevant.


=== RESUME IMPROVEMENTS ===
- Give actionable suggestions based on gaps.
- Do not suggest adding fake experience.

=== INTERVIEW PREPARATION ===
- List technical topics the candidate should prepare for this role.



Resume:
{resume_context}

Job Description:
{job_context}

Analysis:
"""
    return prompt