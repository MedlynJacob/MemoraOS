<div align="center">

# 💾 MemoraOS

### *Your AI Career Operating System*

> An AI-powered career assistant for resume intelligence, job matching, application tracking, and career insights.

🚀 **[Live Demo](https://memoraos.streamlit.app/)**
💻 **[GitHub Repository](https://github.com/MedlynJacob/MemoraOS)**

<img src="https://readme-typing-svg.demolab.com?font=VT323&size=30&pause=1200&color=39FF14&center=true&vCenter=true&width=700&lines=Booting+MemoraOS...;Loading+Career+Engine...;Initializing+AI+Core...;System+Ready" />

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red?style=for-the-badge)
![AI](https://img.shields.io/badge/AI-HuggingFace%20%7C%20Ollama-purple?style=for-the-badge)
![RAG](https://img.shields.io/badge/RAG-Foundation-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-v1.0--Deployed-success?style=for-the-badge)

</div>

---

```text
███╗   ███╗███████╗███╗   ███╗ ██████╗ ██████╗  █████╗  ██████╗ ███████╗
████╗ ████║██╔════╝████╗ ████║██╔═══██╗██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██╔████╔██║█████╗  ██╔████╔██║██║   ██║██████╔╝███████║██║   ██║███████╗
██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██║   ██║██╔══██╗██╔══██║██║   ██║╚════██║
██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║╚██████╔╝██║  ██║██║  ██║╚██████╔╝███████║
╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ══════╝╚══════╝
```

```bash
$ memora boot

Initializing Career Engine...
Loading Resume Intelligence...
Connecting AI Engine...
Checking Career Pipeline...
System Ready.

Welcome back.
```

---

# > whoami

**MemoraOS** is a personal AI career operating system designed to organize, analyze, and improve the software engineering job search process.

The project started as a local-first AI memory system focused on **Retrieval-Augmented Generation (RAG)**. It evolved into a practical career assistant that combines:

* Resume intelligence
* Job description analysis
* Resume-to-job similarity matching
* AI-powered career insights
* Application tracking
* Career analytics

The long-term goal is to build a personal AI system that understands a candidate's experience, projects, skills, applications, and professional growth.

---

# > live demo

🚀 **[Launch MemoraOS](https://memoraos.streamlit.app/)**

The public deployment currently showcases the **Resume Analyzer**.

Upload:

1. Your resume
2. A job description
3. An optional company name

MemoraOS generates:

* Resume ↔ JD match score
* Strong skill matches
* Missing requirements
* Experience gaps
* Relevant projects
* Resume improvement suggestions
* Interview preparation topics

> **Demo note:** Uploaded documents are processed through the AI inference service configured for the public deployment. Avoid uploading confidential or sensitive documents.

---

# > mission status

```text
VERSION 1.0  ████████████████████  DEPLOYED ✅


RESUME INTELLIGENCE

✓ Resume Processing
✓ Job Description Processing
✓ PDF / TXT Extraction
✓ Resume ↔ Job Similarity Analysis
✓ Semantic Embeddings
✓ AI-powered Resume Evaluation
✓ Experience Gap Detection
✓ Resume Improvement Suggestions
✓ Interview Preparation


APPLICATION MANAGEMENT

✓ Add Applications
✓ Edit Applications
✓ Delete Applications
✓ Track Application Status
✓ Track Referrals
✓ Store Notes
✓ Track Locations
✓ Manage Follow-ups


AI FOUNDATION

✓ Ollama Local LLM Integration
✓ Hugging Face Inference Support
✓ Embedding-based Retrieval
✓ RAG Architecture Foundation
✓ Modular AI Pipeline


ANALYTICS

✓ Career Dashboard
✓ Application Pipeline Tracking
✓ Career Progress Overview
```

---

# > architecture

## Resume Analysis Pipeline

```text
                   Resume PDF
                       |
                       ▼
               Document Extraction
                       |
                       ▼
                  Smart Chunking
                       |
                       ▼
                 Embeddings
                       |
                       ▼
             Semantic Similarity
                       |
                       ▼
              Relevant Context
                       |
                       ▼
                LLM Analysis
                       |
                       ▼
              Structured Results
                       |
          ┌────────────┼────────────┐
          ▼            ▼            ▼
     Match Score   Experience    Resume
                    Gaps       Improvements
          │            │            │
          └────────────┼────────────┘
                       ▼
                 Streamlit UI
```

## Application Tracking

```text
User
 |
 ▼
Streamlit Interface
 |
 ▼
Application Manager
 |
 ├── Company
 ├── Role
 ├── Status
 ├── Referral
 ├── Location
 ├── Notes
 └── Follow-up
 |
 ▼
Persistent Storage
```

## Future AI Memory Layer

```text
Documents
    |
    ▼
RAG Pipeline
    |
    ▼
Vector Database
    |
    ▼
Personal AI Memory
    |
    ▼
Career Intelligence
```

---

# > current capabilities

## Resume Intelligence

```text
✓ Upload resumes
✓ Process PDF documents
✓ Process TXT documents
✓ Analyze job descriptions
✓ Generate semantic embeddings
✓ Compare resume against job requirements
✓ Identify strong matches
✓ Identify missing requirements
✓ Identify experience gaps
✓ Recommend resume improvements
✓ Generate interview preparation topics
```

## Application Tracking

```text
✓ Track job applications
✓ Store company information
✓ Store role information
✓ Track application status
✓ Track referrals
✓ Store application notes
✓ Track locations
✓ Manage follow-ups
```

Supported statuses:

```text
Applied
OA Scheduled
OA Completed
Interview
Offer
Rejected
Withdrawn
```

## Analytics

```text
✓ Application dashboard
✓ Application pipeline
✓ Career progress overview
```

---

# > technology stack

```text
LANGUAGE
--------
Python


FRONTEND
--------
Streamlit


AI / ML
-------
Hugging Face Inference
Ollama
Semantic Embeddings
Resume Similarity Analysis
Large Language Models
Retrieval-Augmented Generation (RAG)


EMBEDDINGS
----------
BAAI/bge-small-en-v1.5
nomic-embed-text


DOCUMENT PROCESSING
-------------------
PyPDF
Text Extraction
Document Chunking
Document Modeling


DATA / STORAGE
--------------
JSON Persistence
ChromaDB


ENGINEERING
-----------
Modular Python Architecture
Object-Oriented Design
CRUD Architecture
REST/API Integration
Local-first Development
```

---

# > engineering decisions

## Why local-first?

Career information can contain sensitive data:

* Resumes
* Applications
* Personal notes
* Career history

MemoraOS was designed with a **local-first architecture** so the core system can run locally with locally hosted AI models.

```text
✓ Data ownership
✓ Local experimentation
✓ Offline-capable architecture
✓ Local AI option
✓ Replaceable AI providers
```

The public demo uses a separate cloud inference configuration so the application can be accessed without requiring users to install local AI models.

---

## Why Ollama?

During local development, MemoraOS uses **Ollama** to run AI models locally.

```text
Local Development

MemoraOS
   |
   ▼
Ollama
   |
   ├── Embeddings
   └── Local LLM
```

This allows experimentation with AI models without making the application dependent on a hosted inference API.

---

## Why provider abstraction?

The AI layer is designed so that the application can switch between local and hosted inference.

```text
                 MemoraOS
                    |
              AI Provider
             /           \
            ▼             ▼
        Ollama        Hugging Face
        Local           Cloud
```

This makes the system easier to deploy while preserving the local development workflow.

---

## Why modular architecture?

MemoraOS separates major responsibilities:

```text
Resume
  |
  ▼
Document Processing
  |
  ▼
Chunking
  |
  ▼
Embeddings
  |
  ▼
Retrieval / Similarity
  |
  ▼
AI Analysis
  |
  ▼
Streamlit UI
```

Application management follows a separate path:

```text
Application
  |
  ▼
Application Manager
  |
  ▼
Storage Layer
  |
  ▼
Analytics
```

This separation allows new AI capabilities to be added without rewriting the core application.

---

# > project structure

```text
MemoraOS/
│
├── app/
│   ├── analysis/
│   ├── applications/
│   ├── chatbot/
│   ├── chunking/
│   ├── database/
│   ├── embeddings/
│   ├── indexing/
│   ├── loaders/
│   ├── llm/
│   ├── memory/
│   ├── models/
│   ├── prompts/
│   ├── retrieval/
│   ├── storage/
│   ├── tests/
│   ├── ui/
│   └── app.py
│
├── data/
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── run.py
```

---

# > achievements

```text
🏆 UNLOCKED

✓ Resume Intelligence Engine
✓ Semantic Resume Matching
✓ AI-powered Resume Evaluation
✓ Ollama Local AI Integration
✓ Hugging Face Cloud Inference
✓ Career Application Tracker
✓ Dashboard Analytics
✓ CRUD Application Architecture
✓ Modular Python Architecture
✓ Public Streamlit Deployment


────────────────────────────────────


🔒 NEXT UNLOCKS

Resume Optimization
Resume Version Control
AI Job Recommendations
Advanced Interview Coach
Personal Career Memory
Knowledge Graph
```

---

# > roadmap

```text
v1.0
------
Career Intelligence Foundation

[COMPLETE]


v2.0
------
AI Career Assistant

□ Resume Optimization
□ Resume Version Control
□ AI Job Recommendations
□ Advanced Interview Preparation
□ Career Insights


v3.0
------
Personal AI Memory Operating System

□ Long-term Career Memory
□ Knowledge Graph
□ Project Intelligence
□ Personalized AI Career Companion


COMING SOON
```

---

# > local development

```bash
git clone https://github.com/MedlynJacob/MemoraOS.git

cd MemoraOS

python -m venv venv

source venv/bin/activate
# Windows:
# venv\Scripts\activate

pip install -r requirements.txt

python -m streamlit run app/app.py
```

For local AI development, configure Ollama and the required local models.

For hosted inference, configure the appropriate environment variables using `.env` locally or Streamlit Secrets when deploying.

---

# > system status

```text
Developer     : Medlyn Jacob
Version       : v1.0
Current Mode  : Career Intelligence
Framework     : Streamlit
AI            : Ollama / Hugging Face
Embeddings    : BGE / Ollama
Storage       : JSON / ChromaDB

Status        : ONLINE
```

---

<div align="center">

### ☕ Built with coffee, curiosity, and an unreasonable number of commits.

### 🚀 One commit closer to the dream job.

```bash
> exit

Saving career data...
Writing commits...
Preparing next evolution...

Connection terminated.
```

⭐ **Star the repository if you enjoyed the project.**

</div>
