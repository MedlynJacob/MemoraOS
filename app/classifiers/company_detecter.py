def detect_company(filename: str, text: str) -> str:
    sample = text[:2000].lower()
    companies=["amazon","google","microsoft","apple","meta","ibm","salesforce","nvidia","netflix","tesla"]

    for company in companies:
        if company in sample:
            return company.title()

    return ""