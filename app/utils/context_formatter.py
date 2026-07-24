def format_context(results: dict) -> str:
    documents = results["documents"]
    metadatas = results["metadatas"]

    formatted = []

    for doc, meta in zip(documents, metadatas):
        formatted.append(
            f"""
Document Type: {meta['document_type']}
Company: {meta['company']}
Filename: {meta['filename']}

{doc}
"""
        )

    return "\n\n------------------------\n\n".join(formatted)