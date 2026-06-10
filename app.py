import os
import streamlit as st

try:
    for key, value in st.secrets.items():
        os.environ[key] = str(value)
except Exception:
    pass
import time
from graph.research_graph import graph
from utils.pdf_generator import save_pdf

os.makedirs("outputs", exist_ok=True)

st.set_page_config(
    page_title="Autonomous Research Agent",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background-color: #0e0e11;
    color: #e8e8ed;
}

section[data-testid="stSidebar"] {
    background-color: #13131a;
    border-right: 1px solid #1e1e2e;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.6rem;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.2;
    margin-bottom: 0.3rem;
}

.hero-sub {
    font-size: 1rem;
    color: #7a7a8c;
    font-weight: 400;
    letter-spacing: 0.02em;
    margin-bottom: 2rem;
}

.pipeline-card {
    background: #13131a;
    border: 1px solid #1e1e2e;
    border-radius: 10px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.6rem;
    display: flex;
    align-items: center;
    gap: 0.8rem;
    transition: border-color 0.3s;
}

.pipeline-card.active {
    border-color: #7c6ff7;
    background: #16162a;
}

.pipeline-card.done {
    border-color: #2cb67d;
    background: #0f1a16;
}

.step-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #2a2a3a;
    flex-shrink: 0;
}

.step-dot.active {
    background: #7c6ff7;
    box-shadow: 0 0 8px #7c6ff755;
}

.step-dot.done {
    background: #2cb67d;
}

.step-label {
    font-size: 0.85rem;
    color: #7a7a8c;
    font-weight: 500;
}

.step-label.active { color: #c4bfff; }
.step-label.done   { color: #6ee7b7; }

.metric-box {
    background: #13131a;
    border: 1px solid #1e1e2e;
    border-radius: 10px;
    padding: 1.1rem 1.4rem;
    text-align: center;
}

.metric-num {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 700;
    color: #7c6ff7;
}

.metric-label {
    font-size: 0.78rem;
    color: #7a7a8c;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-top: 0.2rem;
}

.source-card {
    background: #13131a;
    border: 1px solid #1e1e2e;
    border-radius: 8px;
    padding: 0.9rem 1.1rem;
    margin-bottom: 0.5rem;
}

.source-title {
    font-size: 0.9rem;
    font-weight: 600;
    color: #e8e8ed;
    margin-bottom: 0.25rem;
}

.source-meta {
    font-size: 0.76rem;
    color: #7a7a8c;
}

.source-badge {
    display: inline-block;
    font-size: 0.68rem;
    font-weight: 600;
    padding: 0.15rem 0.55rem;
    border-radius: 20px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}

.badge-web   { background: #1a2035; color: #7c9ef7; border: 1px solid #2a3a6a; }
.badge-paper { background: #1a1a35; color: #b07cf7; border: 1px solid #3a2a6a; }

.report-box {
    background: #13131a;
    border: 1px solid #1e1e2e;
    border-radius: 10px;
    padding: 2rem 2.4rem;
    line-height: 1.8;
    font-size: 0.95rem;
    color: #d0d0de;
}

.review-box {
    background: #0f1a16;
    border: 1px solid #1e3028;
    border-radius: 10px;
    padding: 1.2rem 1.6rem;
    font-size: 0.9rem;
    color: #a0c8b8;
    line-height: 1.7;
}

.task-chip {
    display: inline-block;
    background: #16162a;
    border: 1px solid #2a2a4a;
    border-radius: 20px;
    padding: 0.25rem 0.75rem;
    font-size: 0.8rem;
    color: #c4bfff;
    margin: 0.2rem;
}

.divider {
    border: none;
    border-top: 1px solid #1e1e2e;
    margin: 1.5rem 0;
}

.stTextArea textarea {
    background: #13131a !important;
    border: 1px solid #2a2a3a !important;
    color: #e8e8ed !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.95rem !important;
}

.stTextArea textarea:focus {
    border-color: #7c6ff7 !important;
    box-shadow: 0 0 0 2px #7c6ff720 !important;
}

.stButton > button {
    background: linear-gradient(135deg, #7c6ff7, #5a4fd4) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    padding: 0.6rem 1.6rem !important;
    width: 100% !important;
    transition: opacity 0.2s !important;
}

.stButton > button:hover {
    opacity: 0.88 !important;
}

.stDownloadButton > button {
    background: #13131a !important;
    color: #7c6ff7 !important;
    border: 1px solid #7c6ff7 !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    width: 100% !important;
}

.stTabs [data-baseweb="tab"] {
    color: #7a7a8c !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.9rem !important;
}

.stTabs [aria-selected="true"] {
    color: #c4bfff !important;
}

.stTabs [data-baseweb="tab-highlight"] {
    background-color: #7c6ff7 !important;
}

.stTabs [data-baseweb="tab-border"] {
    background-color: #1e1e2e !important;
}
</style>
""", unsafe_allow_html=True)

PIPELINE_STEPS = [
    ("manager",   "🧠", "Manager Agent",   "Breaking query into research tasks"),
    ("search",    "🌐", "Search Agent",    "Searching the web via Tavily"),
    ("paper",     "📄", "Paper Agent",     "Fetching papers from ArXiv"),
    ("rag",       "🗄️", "RAG Agent",       "Storing documents in ChromaDB"),
    ("retriever", "🔍", "Retriever Agent", "Retrieving top-K context"),
    ("writer",    "✍️", "Writer Agent",    "Drafting the research report"),
    ("reviewer",  "✅", "Reviewer Agent",  "Reviewing and finalising report"),
]

with st.sidebar:
    st.markdown("""
        <div style="padding: 0.5rem 0 1.2rem 0;">
            <div style="font-size:1.35rem; font-weight:700; color:#ffffff; font-family:'Playfair Display',serif;">
                🔬 Research Agent
            </div>
            <div style="font-size:0.78rem; color:#7a7a8c; margin-top:0.3rem;">
                Autonomous · Multi-Agent · RAG-Powered
            </div>
        </div>
        <hr style="border:none; border-top:1px solid #1e1e2e; margin-bottom:1.4rem;">
    """, unsafe_allow_html=True)

    st.markdown("<div style='font-size:0.75rem; color:#7a7a8c; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:0.8rem;'>Pipeline</div>", unsafe_allow_html=True)

    active_step = st.session_state.get("active_step", None)
    completed_steps = st.session_state.get("completed_steps", [])

    for step_id, icon, label, desc in PIPELINE_STEPS:
        if step_id in completed_steps:
            state_cls = "done"
        elif step_id == active_step:
            state_cls = "active"
        else:
            state_cls = ""

        st.markdown(f"""
            <div class="pipeline-card {state_cls}">
                <div class="step-dot {state_cls}"></div>
                <div>
                    <div class="step-label {state_cls}">{icon} {label}</div>
                    <div style="font-size:0.72rem; color:#4a4a5a; margin-top:1px;">{desc}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr style='border:none; border-top:1px solid #1e1e2e; margin:1.4rem 0;'>", unsafe_allow_html=True)

    st.markdown("""
        <div style="font-size:0.75rem; color:#4a4a5a; line-height:1.6;">
            <div style="margin-bottom:0.3rem;"><span style="color:#7c6ff7;">●</span> Gemini 2.5 Flash</div>
            <div style="margin-bottom:0.3rem;"><span style="color:#7c9ef7;">●</span> Tavily Search</div>
            <div style="margin-bottom:0.3rem;"><span style="color:#b07cf7;">●</span> ArXiv Papers</div>
            <div><span style="color:#2cb67d;">●</span> ChromaDB Vector Store</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="hero-title">Autonomous Research Agent</div>
    <div class="hero-sub">Multi-agent pipeline · Web + Academic sources · RAG-powered · PDF export</div>
""", unsafe_allow_html=True)

query = st.text_area(
    label="Research Query",
    placeholder="e.g. Future of multimodal large language models in enterprise applications",
    height=90,
    label_visibility="collapsed"
)

run_col, _ = st.columns([1, 3])
with run_col:
    run_button = st.button("Generate Report →")

if run_button:
    if not query.strip():
        st.warning("Please enter a research query before running.")
    else:
        st.session_state["active_step"] = None
        st.session_state["completed_steps"] = []
        st.session_state["result"] = None

        st.markdown("<hr class='divider'>", unsafe_allow_html=True)
        st.markdown("<div style='font-size:0.85rem; color:#7a7a8c; margin-bottom:0.8rem;'>Running pipeline…</div>", unsafe_allow_html=True)

        progress_bar = st.progress(0)
        status_text  = st.empty()
        sidebar_placeholder = st.empty()

        total_steps = len(PIPELINE_STEPS)

        def run_with_progress():
            completed = []
            for i, (step_id, icon, label, desc) in enumerate(PIPELINE_STEPS):
                st.session_state["active_step"]    = step_id
                st.session_state["completed_steps"] = completed.copy()
                progress_bar.progress(int((i / total_steps) * 100))
                status_text.markdown(f"<div style='font-size:0.85rem; color:#c4bfff;'>{icon} {label} — {desc}…</div>", unsafe_allow_html=True)
                time.sleep(0.1)

            result = graph.invoke({"query": query.strip()})

            for step_id, _, _, _ in PIPELINE_STEPS:
                completed.append(step_id)

            st.session_state["active_step"]    = None
            st.session_state["completed_steps"] = completed
            progress_bar.progress(100)
            status_text.markdown("<div style='font-size:0.85rem; color:#2cb67d;'>✓ Pipeline complete</div>", unsafe_allow_html=True)
            return result

        result = run_with_progress()
        st.session_state["result"] = result
        st.session_state["query"]  = query.strip()
        st.rerun()

if st.session_state.get("result"):
    result = st.session_state["result"]
    q      = st.session_state.get("query", "")

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    tasks          = result.get("tasks", [])
    search_results = result.get("search_results", [])
    paper_results  = result.get("paper_results", [])
    sources        = result.get("retrieved_sources", [])
    final_report   = result.get("final_report", "")
    review_comments = result.get("review_comments", "")

    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f'<div class="metric-box"><div class="metric-num">{len(tasks)}</div><div class="metric-label">Research Tasks</div></div>', unsafe_allow_html=True)
    with m2:
        st.markdown(f'<div class="metric-box"><div class="metric-num">{len(search_results)}</div><div class="metric-label">Web Articles</div></div>', unsafe_allow_html=True)
    with m3:
        st.markdown(f'<div class="metric-box"><div class="metric-num">{len(paper_results)}</div><div class="metric-label">ArXiv Papers</div></div>', unsafe_allow_html=True)
    with m4:
        st.markdown(f'<div class="metric-box"><div class="metric-num">{len(sources)}</div><div class="metric-label">RAG Sources</div></div>', unsafe_allow_html=True)

    st.markdown("<div style='margin-top:1.6rem;'></div>", unsafe_allow_html=True)

    tab_report, tab_sources, tab_review = st.tabs(["📋  Final Report", "📚  Sources", "🔎  Review Notes"])

    with tab_report:
        st.markdown("<div style='margin-top:1rem;'></div>", unsafe_allow_html=True)

        if tasks:
            st.markdown("<div style='font-size:0.78rem; color:#7a7a8c; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.5rem;'>Research Tasks</div>", unsafe_allow_html=True)
            chips = "".join([f'<span class="task-chip">{t}</span>' for t in tasks])
            st.markdown(f"<div style='margin-bottom:1.2rem;'>{chips}</div>", unsafe_allow_html=True)

        st.markdown(f'<div class="report-box">{final_report.replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)

        st.markdown("<div style='margin-top:1.2rem;'></div>", unsafe_allow_html=True)

        pdf_path = "outputs/report.pdf"
        save_pdf(final_report, pdf_path)

        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()

        st.download_button(
            label="Download PDF Report",
            data=pdf_bytes,
            file_name=f"research_report_{q[:40].replace(' ', '_')}.pdf",
            mime="application/pdf"
        )

    with tab_sources:
        st.markdown("<div style='margin-top:1rem;'></div>", unsafe_allow_html=True)

        web_sources   = [s for s in sources if s.get("type") == "web"]
        paper_sources = [s for s in sources if s.get("type") == "paper"]

        if web_sources:
            st.markdown("<div style='font-size:0.78rem; color:#7a7a8c; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.6rem;'>Web Sources</div>", unsafe_allow_html=True)
            for s in web_sources:
                url = s.get("source", "#")
                st.markdown(f"""
                    <div class="source-card">
                        <div class="source-title">{s.get("title", "Untitled")}</div>
                        <div class="source-meta" style="margin-top:0.3rem;">
                            <span class="source-badge badge-web">Web</span>
                            &nbsp;<a href="{url}" target="_blank" style="color:#7c9ef7; font-size:0.76rem; text-decoration:none;">{url[:70]}{'…' if len(url)>70 else ''}</a>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

        if paper_sources:
            st.markdown("<div style='font-size:0.78rem; color:#7a7a8c; text-transform:uppercase; letter-spacing:0.08em; margin:1rem 0 0.6rem 0;'>ArXiv Papers</div>", unsafe_allow_html=True)
            for s in paper_sources:
                url = s.get("source", "#")
                st.markdown(f"""
                    <div class="source-card">
                        <div class="source-title">{s.get("title", "Untitled")}</div>
                        <div class="source-meta" style="margin-top:0.15rem;">
                            {s.get("authors", "")}
                        </div>
                        <div class="source-meta" style="margin-top:0.3rem;">
                            <span class="source-badge badge-paper">Paper</span>
                            &nbsp;<span style="color:#5a5a6a;">{s.get("published","")}</span>
                            &nbsp;&nbsp;<a href="{url}" target="_blank" style="color:#b07cf7; font-size:0.76rem; text-decoration:none;">PDF ↗</a>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

    with tab_review:
        st.markdown("<div style='margin-top:1rem;'></div>", unsafe_allow_html=True)
        if review_comments:
            st.markdown(f'<div class="review-box">{review_comments.replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)
        else:
            st.markdown("<div style='color:#4a4a5a; font-size:0.9rem;'>No review comments available.</div>", unsafe_allow_html=True)
