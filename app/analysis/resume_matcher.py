from retrieval.retrieval import retrieve


def get_resume_and_jd(company: str):
    resume = retrieve(
        query="my resume",
        document_type="resume",
        top_k=7,
    )

    job_description = retrieve(
        query="job description",
        document_type="job_description",
        company=company,
        top_k=7,
    )

    return resume, job_description