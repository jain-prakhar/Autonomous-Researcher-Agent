from llm import llm


def reviewer_agent(state):

    report = state["draft_report"]
    sources = state["retrieved_sources"]

    prompt = f"""
You are a senior research reviewer.

Review the following report.

Requirements:
- Improve clarity, structure, and accuracy.
- Do NOT invent citations, references, URLs, authors, or sources.
- Do NOT add a References section.
- Preserve all factual information from the report.

Return your response EXACTLY in this format:

REVIEW_COMMENTS:
<your review comments>

FINAL_REPORT:
<improved report>

REPORT:
{report}
"""

    response = llm.invoke(prompt)

    text = response.content

    review_comments = ""
    final_report = text

    if "FINAL_REPORT:" in text:

        parts = text.split("FINAL_REPORT:")

        review_comments = (
            parts[0]
            .replace("REVIEW_COMMENTS:", "")
            .strip()
        )

        final_report = parts[1].strip()

    # Build references from retrieved metadata
    references = []
    seen_sources = set()

    for source in sources:

        source_url = source.get("source", "")

        if source_url in seen_sources:
            continue

        seen_sources.add(source_url)

        ref = f"{len(references)+1}. {source.get('title', 'Unknown Title')}"

        if source.get("authors"):
            ref += f"\n   Authors: {source['authors']}"

        if source.get("published"):
            ref += f"\n   Published: {source['published']}"

        ref += f"\n   Source: {source_url}"

        references.append(ref)

    references_text = "\n\n".join(references)

    final_report += f"""

# References

{references_text}
"""

    return {
        "review_comments": review_comments,
        "final_report": final_report
    }