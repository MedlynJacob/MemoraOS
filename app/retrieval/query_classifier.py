def detect_document_type(query: str) -> str | None:
    query = query.lower()

    resume_keywords = [
        "my",
        "resume",
        "project",
        "experience",
        "worked",
        "skills",
        "internship",
        "education",
    ]

    job_keywords = [
        "job description",
        "job",
        "role",
        "position",
        "requirements",
        "responsibilities",
    ]

    if any(word in query for word in resume_keywords):
        return "resume"

    if any(word in query for word in job_keywords):
        return "job_description"

    return None