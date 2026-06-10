# 🔬 Autonomous Research Agent

A multi-agent AI system that takes a research question and autonomously produces a structured, cited research report — pulling from live web sources and academic papers, storing them in a vector database, and synthesising everything through a chain of specialised LLM agents.

Built with **LangGraph**, **Gemini 2.5 Flash**, **Tavily**, **ArXiv**, **ChromaDB**, and **Streamlit**.

---

## How It Works

The system runs a sequential multi-agent pipeline orchestrated by LangGraph. Each agent has a single responsibility and passes its output forward as shared state.

```
Query → Manager → Search → Paper → RAG → Retriever → Writer → Reviewer → Report
```

| Agent | Role |
|---|---|
| 🧠 **Manager** | Breaks the query into 5–8 focused research sub-tasks |
| 🌐 **Search** | Runs each sub-task through Tavily to fetch live web results |
| 📄 **Paper** | Queries ArXiv for the 10 most relevant academic papers |
| 🗄️ **RAG** | Embeds all documents into a ChromaDB vector store |
| 🔍 **Retriever** | Retrieves the top-10 most relevant chunks for the original query |
| ✍️ **Writer** | Drafts a 7-section research report using only retrieved context |
| ✅ **Reviewer** | Improves clarity and structure, then appends a verified reference list |

The final output is displayed in a Streamlit UI and exported as a downloadable PDF.

---

## Features

- **Grounded writing** — the Writer agent is instructed not to invent any facts, statistics, URLs, or author names; everything comes from retrieved sources
- **Dual source types** — combines live web results (Tavily) with peer-reviewed papers (ArXiv)
- **RAG pipeline** — ChromaDB stores and retrieves the most relevant context via semantic search
- **Automated review** — a Reviewer agent improves the draft and builds the reference list from actual retrieved metadata
- **PDF export** — download the final report as a formatted PDF
- **Live pipeline status** — the sidebar shows each agent activating and completing in real time

---

## Project Structure

```
├── app.py                  # Streamlit UI
├── main.py                 # CLI entry point
├── state.py                # Shared LangGraph state schema
├── llm.py                  # Gemini 2.5 Flash client
├── requirements.txt
│
├── agents/
│   ├── manager.py          # Task decomposition agent
│   ├── search_agent.py     # Tavily web search agent
│   ├── paper_agent.py      # ArXiv paper fetch agent
│   ├── rag_agent.py        # ChromaDB ingestion agent
│   ├── retriever_agent.py  # Semantic retrieval agent
│   ├── writer_agent.py     # Report drafting agent
│   └── reviewer_agent.py   # Review + reference agent
│
├── graph/
│   └── research_graph.py   # LangGraph pipeline definition
│
├── rag/
│   ├── vector_store.py     # ChromaDB client + document storage
│   └── retriever.py        # Query + retrieval logic
│
└── utils/
    └── pdf_generator.py    # ReportLab PDF export
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| LLM | Gemini 2.5 Flash (via LangChain) |
| Agent Orchestration | LangGraph |
| Web Search | Tavily |
| Academic Papers | ArXiv |
| Vector Store | ChromaDB |
| Embeddings | ChromaDB default (all-MiniLM) |
| UI | Streamlit |
| PDF Generation | ReportLab |

---

## Setup

### 1. Clone and install

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
pip install -r requirements.txt
```

### 2. Configure API keys

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Get your keys here:
- **Google API key** — [aistudio.google.com](https://aistudio.google.com)
- **Tavily API key** — [tavily.com](https://tavily.com)

### 3. Run

**Streamlit UI:**
```bash
streamlit run app.py
```

**CLI (outputs PDF to `outputs/report.pdf`):**
```bash
python main.py
```

---


