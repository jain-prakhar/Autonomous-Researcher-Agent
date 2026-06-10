from rag.vector_store import store_documents
from rag.vector_store import collection


def rag_agent(state):

    documents = []

    for result in state["search_results"]:

        content = result.get("content", "")

        if content:

            documents.append(
                {
                "content": content,
                "title": result.get("title", "Unknown"),
                "source": result.get("url", ""),
                "type": "web"
            }
            )

    for paper in state["paper_results"]:

        # FIX 1: paper_agent stores the text under "content", not "summary"
        content = paper.get("content", "")

        if content:

            documents.append(
                {
                # FIX 1: use "content" key (was "summary" — always empty → 0 papers stored)
                "content": content,
                "title": paper.get("title", "Unknown"),
                # FIX 2: authors is already a joined string from paper_agent,
                #         calling ", ".join() on a string iterates over characters
                "authors": paper.get("authors", ""),
                "published": paper.get("published", ""),
                # FIX 3: paper_agent stores the URL under "source", not "pdf_url"
                "source": paper.get("source", ""),
                "type": "paper"
            }
            )

    try:
        existing = collection.get()

        if existing["ids"]:
            collection.delete(ids=existing["ids"])

    except Exception as e:
        print(f"Collection clear warning: {e}")

    if documents:
        store_documents(documents)

    return {}
