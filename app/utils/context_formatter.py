def format_context(results: dict) -> str:
    documents = results["documents"]
    metadatas = results["metadatas"]

    formatted = []

    for doc, meta in zip(documents, metadatas):
        formatted.append(
            f"""
Document Type: {meta.get('document_type', 'Unknown')}
Company: {meta.get('company', 'Not specified')}
Filename: {meta.get('filename', 'Unknown')}

{doc}
"""
        )

    return "\n\n------------------------\n\n".join(formatted)