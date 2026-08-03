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
    result = {}

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

    # Clean whitespace
    for key in result:
        result[key] = result[key].strip()

    # Extract numeric score
    if "score" in result:
        score = result["score"].replace("%", "").strip()
        result["score"] = score
    else:
        result["score"] = "N/A"

    return result