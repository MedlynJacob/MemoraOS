#To find the document type 
def detect_document_type(filename: str, text: str) -> str:
    name = filename.lower()
    sample = text.lower()

    # Resume detection
    if "resume" in name or "cv" in name:
        return "resume"

    if all(keyword in sample for keyword in [
        "education",
        "experience",
        "skills"
    ]):
        return "resume"

    # Job description detection
    if any(keyword in sample for keyword in [
        "responsibilities",
        "qualifications",
        "requirements",
        "preferred qualifications"
    ]):
        return "job_description"
    
    if any(keyword in sample for keyword in [
    "installation",
    "usage",
    "features",
    "tech stack",
    "architecture"
    ]):
        return "project"

    return "unknown"
