import arxiv

from state import ResearchState


def paper_agent(state: ResearchState):

    query = state["query"]

    paper_results = []

    try:

        client = arxiv.Client()

        search = arxiv.Search(
            query=query,
            max_results=10,
            sort_by=arxiv.SortCriterion.Relevance
        )

        for paper in client.results(search):

            paper_results.append(
                {
    "content": paper.summary[:1000],
    "source": paper.pdf_url,
    "title": paper.title,
    "authors": ", ".join(
        author.name for author in paper.authors
    ),
    "published": str(
        paper.published.date()
    ),
    "type": "paper"
}
            )

    except Exception as e:

        print(f"Paper search error: {e}")

    return {
        "paper_results": paper_results
    }