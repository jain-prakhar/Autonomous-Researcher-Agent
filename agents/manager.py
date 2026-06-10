import json

from llm import llm
from state import ResearchState


def manager_agent(state: ResearchState):

    query = state["query"]

    prompt = f"""
You are a research manager.

Your task is to break a research question into
5-8 independent research tasks.

Return ONLY valid JSON.

Example:

{{
    "tasks": [
        "Current applications",
        "Benefits",
        "Challenges",
        "Future trends"
    ]
}}

Research Query:
{query}
"""

    response = llm.invoke(prompt)


    try:
        content = response.content.strip()

        # Remove markdown code blocks if Gemini adds them
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

        data = json.loads(content)

        return {
            "tasks": data["tasks"]
        }

    except Exception as e:

        print("JSON PARSING ERROR:")
        print(e)

        return {
            "tasks": [
                "Introduction",
                "Applications",
                "Benefits",
                "Challenges",
                "Future Trends"
            ]
        }