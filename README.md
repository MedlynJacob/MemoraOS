<div align="center">

# 💾 MemoraOS

### *Your AI Second Brain for Learning, Building, and Career Growth*
> **A local-first AI memory operating system that turns resumes, projects, notes, and job descriptions into a searchable conversational knowledge base powered by Retrieval-Augmented Generation (RAG).**

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
Detecting Document Types...
Generating Embeddings...
Connecting ChromaDB...
Loading Conversation Memory...
Local LLM Connected.

System Ready.

Welcome back.
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
                        │
                        ▼
                Document Loader
                        │
        ┌───────────────┴───────────────┐
        ▼                               ▼
 Detect Document Type           Detect Company
        │                               │
        └───────────────┬───────────────┘
                        ▼
                Document Objects
                        │
                        ▼
                 Chunking Engine
                        │
                        ▼
              Text Chunks + Metadata
                        │
                        ▼
            Ollama Embedding Pipeline
                        │
                        ▼
                  ChromaDB Storage
                        │
                        ▼
              Metadata-aware Retrieval
                        │
                        ▼
               Context Formatter
                        │
                        ▼
               Prompt Generation
                        │
                        ▼
                Ollama Local LLM
                        │
                        ▼
                 Conversational AI
```

---

# > mission status

```text
LEVEL 1 ████████████████████ COMPLETE ✅

✓ Document Model
✓ PDF/TXT Loader
✓ Recursive File Ingestion
✓ Automatic Document Type Detection
✓ Company Detection
✓ Metadata Tracking


LEVEL 2 ████████████████████ COMPLETE ✅

✓ Chunk Model
✓ Overlapping Text Chunking
✓ UUID Document-Chunk Linking
✓ Ollama Embedding Pipeline
✓ ChromaDB Persistent Storage
✓ Metadata-aware Vector Storage


LEVEL 3 ████████████████████ COMPLETE ✅

✓ Semantic Search
✓ Metadata Filtering
✓ RAG Generation Pipeline
✓ Local LLM Integration
✓ Context-aware Responses
✓ Conversation Memory


LEVEL 4 ███░░░░░░░░░░░░░░░░

□ Resume Intelligence
□ Resume ↔ Job Matching
□ Interview Coach
□ Job Tracker
□ Career Analytics
```

---

# > current capabilities

MemoraOS can currently:

```text
✓ Ingest PDF and TXT documents

✓ Automatically classify documents
    - Resume
    - Job Description

✓ Detect associated companies

✓ Store rich metadata

✓ Split documents into overlapping chunks

✓ Generate semantic embeddings locally

✓ Store vectors in ChromaDB

✓ Perform metadata-aware semantic retrieval

✓ Maintain conversation history

✓ Generate grounded responses using a local LLM

✓ Refuse to hallucinate when information is unavailable
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
Retrieval-Augmented Generation (RAG)
Prompt Engineering
Metadata-aware Semantic Search


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

✓ Document Loader

✓ Automatic Metadata Extraction

✓ PDF Processing Pipeline

✓ UUID Document Model

✓ UUID Chunk Model

✓ Recursive Document Ingestion

✓ Overlapping Chunking

✓ Ollama Embedding Pipeline

✓ ChromaDB Integration

✓ Metadata-aware Semantic Search

✓ Local RAG Chatbot

✓ Conversation Memory

✓ Grounded Responses


────────────────────────────


🔒 LOCKED

Resume Match Analysis

Resume Tailoring

Interview Coach

Application Tracker

Knowledge Graph

Long-term Memory

Offer Letter :)
``` 

---

# > roadmap

```text
v0.1
------
Local RAG Foundation
[COMPLETE]


v0.2
------
Resume Intelligence
[IN PROGRESS]


v0.3
------
Career Assistant
[PLANNED]


v1.0
------
Personal AI Memory Operating System
[COMING SOON]
```

---

# > system status

```text
Developer     : Medlyn Jacob

Version       : v0.2-alpha

Engine        : Ollama

Embeddings    : nomic-embed-text

Database      : ChromaDB

Coffee        : ███████████████░

Motivation    : ████████████████

Sleep         : NULL

Status        : Online
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
