SECTION_HEADERS = {
    "=== MATCH SCORE ===": "score",
    "=== STRONG MATCHES ===": "strong_matches",
    "=== MISSING REQUIREMENTS ===": "missing_requirements",
    "=== EXPERIENCE GAPS ===": "experience_gaps",
    "=== RELEVANT PROJECTS ===": "projects",
    "=== RESUME IMPROVEMENTS ===": "resume_improvements",
    "=== INTERVIEW PREPARATION ===": "interview_preparation",
}


def parse_analysis(analysis: str) -> dict:
    result = {
        "score": "N/A",
        "strong_matches": "None",
        "missing_requirements": "None",
        "experience_gaps": "None",
        "projects": "None",
        "resume_improvements": "None",
        "interview_preparation": "None",
    }

    if not analysis:
        return result

    current_section = None

    for line in analysis.splitlines():
        line = line.strip()

        if not line:
            continue

        if line in SECTION_HEADERS:
            current_section = SECTION_HEADERS[line]
            result[current_section] = ""
            continue

        if current_section:
            result[current_section] += line + "\n"

    for key in result:
        result[key] = result[key].strip()

        if not result[key]:
            result[key] = "None"

    if result["score"] != "N/A":
        result["score"] = (
            result["score"]
            .replace("%", "")
            .strip()
        )

    return result