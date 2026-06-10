from llm import llm
from state import ResearchState


def writer_agent(state: ResearchState):

    query = state["query"]

    context = state["retrieved_context"]
    sources = state["retrieved_sources"]

    source_text = ""

    for i, source in enumerate(sources, start=1):

        source_text += f"""
Source {i}

Title: {source.get('title', 'Unknown')}

Source URL: {source.get('source', 'Unknown')}

Authors: {source.get('authors', 'N/A')}

Published: {source.get('published', 'N/A')}

Type: {source.get('type', 'Unknown')}
--------------------------------------------------
"""

    prompt = f"""
You are an expert research writer.

Research Topic:
{query}

Retrieved Context:
{context}

Available Sources:
{source_text}

Write a professional research report with the following sections:

1. Executive Summary
2. Introduction
3. Key Findings
4. Benefits
5. Challenges
6. Future Trends
7. Conclusion

Requirements:

- Use ONLY information from the Retrieved Context.
- Do NOT invent facts, statistics, studies, papers, URLs, authors, dates, or sources.
- Use only the sources listed in Available Sources.
- If information is missing, explicitly acknowledge the limitation.
- Do not create a References section.
- Do not create placeholder citations.
- Do not mention sources that are not present in Available Sources.
- Write in a formal research-report style.
- Use clear headings and subheadings.
- Synthesize information from multiple retrieved sources where appropriate.
- Be detailed and comprehensive.
"""

    response = llm.invoke(prompt)

    return {
        "draft_report": response.content
    }