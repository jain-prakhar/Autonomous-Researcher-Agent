from tavily import TavilyClient
from dotenv import load_dotenv
import os

from state import ResearchState

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def search_agent(state: ResearchState):

    tasks = state["tasks"]

    search_results = []

    for task in tasks:

        response = client.search(
            query=task,
            max_results=3
        )

        for result in response["results"]:

            search_results.append(
                {
                    "task": task,
                    "title": result["title"],
                    "source": result["url"],
                    "url": result["url"],
                    "type": "web",
                    "content": result["content"]
}
            )

    return {
        "search_results": search_results
    }