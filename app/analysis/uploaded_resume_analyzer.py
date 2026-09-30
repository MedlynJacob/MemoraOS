from io import BytesIO
from datetime import datetime

import numpy as np
from pypdf import PdfReader
from sklearn.metrics.pairwise import cosine_similarity

from models.document import Document
from chunking.smart_chunker import smart_chunking
from embeddings.embeddings_model import (
    generate_embeddings,
    generate_query_embedding,
)
from llm.ollama_client import generate_response
from prompts.resume_analysis_prompt import build_resume_analysis_prompt
from utils.context_formatter import format_context


def extract_uploaded_text(uploaded_file) -> str:
    """Extract text from an uploaded PDF or TXT file."""

    file_bytes = uploaded_file.getvalue()

    if not file_bytes:
        raise ValueError(f"{uploaded_file.name} is empty.")

    filename = uploaded_file.name.lower()

    if filename.endswith(".pdf"):
        reader = PdfReader(BytesIO(file_bytes))

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    elif filename.endswith(".txt"):
        text = file_bytes.decode("utf-8")

    else:
        raise ValueError(
            "Unsupported file type. Please upload a PDF or TXT file."
        )

    if not text.strip():
        raise ValueError(
            f"Could not extract readable text from {uploaded_file.name}."
        )

    return text


def create_document(uploaded_file, document_type: str) -> Document:
    """Convert an uploaded file into a MemoraOS Document."""

    text = extract_uploaded_text(uploaded_file)

    return Document(
        filename=uploaded_file.name,
        filepath="uploaded",
        filetype=uploaded_file.name.split(".")[-1].lower(),
        text=text,
        document_type=document_type,
        indexed_at=datetime.now(),
    )


def retrieve_relevant_chunks(document, query, top_k=7):
    """
    Chunk a document, generate embeddings, and return
    the chunks most relevant to the query.
    """

    chunks = smart_chunking(document)

    if not chunks:
        raise ValueError(
            f"No usable text chunks were created from {document.filename}."
        )

    embeddings = generate_embeddings(chunks)

    query_vector = generate_query_embedding(query)

    chunk_vectors = [
        embedding.vector
        for embedding in embeddings
    ]

    similarities = cosine_similarity(
        [query_vector],
        chunk_vectors
    )[0]

    ranked = sorted(
        zip(chunks, similarities),
        key=lambda item: item[1],
        reverse=True
    )

    selected = ranked[:top_k]

    return {
        "documents": [
            chunk.text
            for chunk, _ in selected
        ],
        "metadatas": [
            {
                "filename": document.filename,
                "document_type": document.document_type,
                "chunk_index": chunk.chunk_index,
            }
            for chunk, _ in selected
        ],
        "similarities": [
            float(score * 100)
            for _, score in selected
        ],
    }


def analyze_uploaded_documents(
    resume_file,
    job_description_file,
    company: str = ""
):
    """Analyze an uploaded resume against an uploaded job description."""

    resume_document = create_document(
        resume_file,
        "resume"
    )

    job_document = create_document(
        job_description_file,
        "job_description"
    )

    resume_results = retrieve_relevant_chunks(
        resume_document,
        "candidate skills, experience, education, projects, and qualifications",
        top_k=7,
    )

    job_results = retrieve_relevant_chunks(
        job_document,
        "required skills, qualifications, responsibilities, experience, and technologies",
        top_k=7,
    )

    resume_context = format_context(resume_results)
    job_context = format_context(job_results)

    prompt = build_resume_analysis_prompt(
        resume_context,
        job_context
    )

    if company.strip():
        prompt += f"\n\nCompany: {company}"

    analysis = generate_response(prompt)

    print("Generated analysis type:", type(analysis))
    print("Generated analysis:", repr(analysis))

    if not analysis:
        raise RuntimeError("The AI model returned an empty analysis.")

    return analysis