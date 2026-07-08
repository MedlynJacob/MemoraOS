<div align="center">

# 💾 MEMORAOS

### *Your AI Second Brain for Learning, Building, and Career Growth*

<img src="https://readme-typing-svg.demolab.com?font=VT323&size=30&pause=1200&color=39FF14&center=true&vCenter=true&width=700&lines=Booting+MemoraOS...;Loading+Memory+Engine...;Connecting+AI+Core...;Ready." />

<br>

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge)
![AI](https://img.shields.io/badge/AI-Powered-purple?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Building-success?style=for-the-badge)
![RAG](https://img.shields.io/badge/RAG-Pipeline-orange?style=for-the-badge)

</div>

---

```ansi
███╗   ███╗███████╗███╗   ███╗ ██████╗ ██████╗  █████╗  ██████╗ ███████╗
████╗ ████║██╔════╝████╗ ████║██╔═══██╗██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██╔████╔██║█████╗  ██╔████╔██║██║   ██║██████╔╝███████║██║   ██║███████╗
██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██║   ██║██╔══██╗██╔══██║██║   ██║╚════██║
██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║╚██████╔╝██║  ██║██║  ██║╚██████╔╝███████║
╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ══════╝╚══════╝
```

```bash
$ memora boot

Initializing Memory Engine...
Loading Documents...
Generating Embeddings...
Connecting Vector Database...
System Ready.

Welcome back, Medlyn.
```

---

# > whoami

**MemoraOS** is a local-first AI memory system designed to organize and retrieve knowledge from my software engineering journey.

Instead of manually searching through:

* Resume versions
* Technical notes
* Project documentation
* Code explanations
* Learning material

MemoraOS aims to provide an intelligent interface where I can ask:

```bash
> Which resume did I send to Amazon?

> Summarize my Operating Systems notes.

> Match my resume to this job description.

> Generate interview questions based on my projects.

> Explain the code I wrote six months ago.
```

The goal is to build a personal AI second brain that grows with every document, project, and experience.

---

# > architecture

```text

                    Documents
                        |
                        v
                Document Loader
                        |
                        v
                Document Objects
                        |
                        v
                 Chunking Engine
                        |
                        v
              Text Chunks + Metadata
                        |
                        v
            Ollama Embedding Pipeline
                        |
                        v
              Vector Representations
                        |
                        v
                  ChromaDB
                        |
                        v
             Semantic Retrieval
                        |
                        v
                  LLM Response


```

---

# > mission status

```text
LEVEL 1 ████████████████████ COMPLETE ✅

✓ Document Model
✓ PDF/TXT Loader
✓ Recursive File Ingestion
✓ Document Metadata Tracking


LEVEL 2 ████████████████████ COMPLETE ✅

✓ Chunk Model
✓ Text Chunking with Overlap
✓ UUID Based Document-Chunk Linking
✓ Ollama Embedding Pipeline
✓ 768 Dimension Vector Generation
✓ ChromaDB Persistent Storage


LEVEL 3 ████████░░░░░░░░░░░░

✓ Semantic Search
□ RAG Generation Pipeline
□ Local LLM Integration
□ Context-Aware Responses
□ Conversation Memory


LEVEL 4

□ Resume Intelligence
□ Job Description Matching
□ Interview Coach
□ Job Tracker
□ Career Analytics

```

---

# > current capabilities

MemoraOS can currently:

```text
✓ Ingest PDF documents

✓ Extract and store document metadata

✓ Split documents into meaningful overlapping chunks

✓ Generate semantic embeddings using Ollama

✓ Store vectors in ChromaDB

✓ Perform similarity-based retrieval

✓ Trace retrieved chunks back to original documents

```

Example:

```bash
Query:

"Machine Learning"


Retrieved:

Result #1
------------------------------
Resume Section:
Machine Learning, Deep Learning,
Computer Vision, NLP, RAG...


Result #2
------------------------------
Education:
Relevant Coursework:
Machine Learning,
Artificial Intelligence...

```

---

# > technology stack

```text
Language
---------
Python


AI / ML
---------
Ollama
nomic-embed-text
Vector Embeddings
Retrieval-Augmented Generation


Storage
---------
ChromaDB
Persistent Vector Database


Document Processing
---------
PyPDF
Custom Document Loader


Architecture Concepts
---------
UUID Based Entity Tracking
Metadata Storage
Semantic Search
Vector Similarity
Modular AI Pipeline

```

---

# > project structure

```text
MemoraOS
│
├── data/
│   └── documents
│
├── storage/
│   └── chroma_db
│
├── app/
│   │
│   ├── loaders/
│   │   └── document_loader.py
│   │
│   ├── models/
│   │   ├── document.py
│   │   ├── chunk.py
│   │   └── embeddings.py
│   │
│   ├── chunking/
│   │   └── text_splitter.py
│   │
│   ├── embeddings/
│   │   └── embeddings.py
│   │
│   ├── database/
│   │   └── chroma_manager.py
│   │
│   ├── retrieval/
│   │
│   ├── tests/
│   │
│   └── main.py
│
└── README.md

```

---

# > engineering decisions

## Why UUIDs?

MemoraOS follows database-style entity relationships.

A document owns multiple chunks:

```text
Document
    |
    |
    +---- Chunk 0
    |
    +---- Chunk 1
    |
    +---- Chunk 2

```

Each chunk stores the parent document ID, allowing retrieval results to trace back to the original source.

---

## Why ChromaDB?

Traditional databases store structured information.

MemoraOS needs to answer questions based on meaning, not exact keywords.

Example:

Searching:

```text
"AI projects"
```

should retrieve:

```text
"Machine Learning Model for Sleep Apnea Detection"

```

even though the words are different.

Vector databases allow this semantic understanding.

---

# > achievements

```text
🏆 UNLOCKED


✓ First Commit

✓ Document Loader

✓ PDF Processing Pipeline

✓ UUID Document Model

✓ UUID Chunk Model

✓ Overlapping Text Chunking

✓ Ollama Embedding Pipeline

✓ 768 Dimension Vector Generation

✓ ChromaDB Vector Storage

✓ Semantic Retrieval


──────────────────────────


🔒 LOCKED


RAG Generation

Memory Consolidation

Resume Intelligence

Interview Coach

Job Tracker

Offer Letter :)

```

---

# > roadmap

```text

Phase 1
-------
Document Intelligence
[COMPLETE]


Phase 2
-------
Semantic Memory
[COMPLETE]


Phase 3
-------
AI Reasoning Layer
[IN PROGRESS]


Phase 4
-------
Career Intelligence Platform
[PLANNED]

```

---

# > system status

```text
Developer    : Medlyn Jacob

Version      : v0.2-alpha

Coffee       : ██████████████░░

Motivation   : ████████████████

Sleep        : NULL

Status       : Building...

```

---

<div align="center">

### ☕ Built with coffee, curiosity, and an unreasonable number of commits.

### 🚀 One commit closer to the dream job.

```bash
> exit

Saving memories...
Writing commits...
See you in the next build.

Connection terminated.
```

⭐ **Star the repository if you enjoyed the journey.**

</div>
