<div align="center">

# 🧠 MemoraOS

### *Building an Operating System for AI Memory*

*"Not another chatbot. The memory behind one."*

---

```text
╔══════════════════════════════════════════════════════╗
║                  MEMORA OS v0.1                      ║
║          Booting AI Memory Operating System...       ║
╚══════════════════════════════════════════════════════╝

[✓] Initializing Project
[✓] Loading Document Ingestion Module
[ ] Loading Document Models
[ ] Initializing Chunking Engine
[ ] Initializing Embedding Engine
[ ] Connecting Vector Database
[ ] Starting Semantic Retrieval
[ ] Launching Memory Engine

System Status : ONLINE
Completion    : 15%
```

</div>

---

# What is MemoraOS?

MemoraOS is my attempt to build a modular AI memory system from scratch.

Instead of building another Retrieval-Augmented Generation (RAG) chatbot, this project focuses on building the **memory architecture** that powers intelligent AI assistants.

The goal is to design a scalable system capable of:

- 📄 Understanding documents
- ✂️ Breaking them into meaningful chunks
- 🧠 Generating semantic embeddings
- 🔍 Retrieving relevant knowledge
- 💬 Providing persistent memory for AI applications

Everything is being implemented incrementally with a focus on clean software architecture rather than simply using libraries.

---

# Current Architecture

```text
                  Raw Documents
                        │
                        ▼
              Document Ingestion
                        │
                        ▼
                 Document Objects
                        │
                        ▼
                 Chunking Engine
                        │
                        ▼
              Embedding Generation
                        │
                        ▼
                 Vector Database
                        │
                        ▼
               Semantic Retrieval
                        │
                        ▼
                 Large Language Model
```

---

# Development Roadmap

## Phase 1 — Foundation

- [x] Project Setup
- [x] Modular Folder Structure
- [x] Document Loader
- [ ] Document Dataclass
- [ ] Chunking Pipeline

---

## Phase 2 — Knowledge Processing

- [ ] Text Embeddings
- [ ] Metadata Management
- [ ] ChromaDB Integration
- [ ] Semantic Search

---

## Phase 3 — Memory Engine

- [ ] Conversation Memory
- [ ] Context Management
- [ ] Memory Ranking
- [ ] Long-Term Memory
- [ ] Intelligent Retrieval

---

# Current Project Structure

```text
MemoraOS/

├── app/
│   ├── loaders/
│   ├── chunking/
│   ├── embeddings/
│   ├── retrieval/
│   ├── database/
│   └── config.py
│
├── data/
│
├── tests/
│
└── README.md
```

---

# Engineering Goals

This project emphasizes:

- Clean Software Architecture
- Modular Python Design
- Information Retrieval
- Vector Databases
- Retrieval-Augmented Generation (RAG)
- AI Memory Systems

Every feature is being implemented step by step rather than relying on end-to-end frameworks.

---

# Current Module

```text
Module Name

Document Ingestion Pipeline

Status

COMPLETE

Responsibilities

✓ Load PDF Documents
✓ Load TXT Documents
✓ Validate Input Files
✓ Extract Text
✓ Generate Metadata
✓ Recursive Folder Traversal
```

---

# Next Mission

```text
Initializing Module...

> Document Dataclass

Objectives

• Create the core Document model
• Introduce Python dataclasses
• Add type hints
• Prepare for chunk generation
```

---

# Why I'm Building This

Most AI projects focus on generating responses.

I wanted to understand **how AI systems remember information**.

MemoraOS is my way of exploring the engineering behind AI memory by implementing every major component—from document ingestion to semantic retrieval—one module at a time.

---

# Project Status

```text
System Health

██████░░░░░░░░░░░░░░░░░░░░░░░░░░░ 15%

Current Version

v0.1

Latest Completed Module

✔ Document Ingestion Pipeline

Next Target

➜ Document Dataclass
```

---

## Built with curiosity ☕ and lots of debugging.
