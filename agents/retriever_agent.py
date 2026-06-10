from rag.retriever import retrieve


def retriever_agent(state):

    query = state["query"]

    docs = retrieve(
        query=query,
        k=10
    )

    context_parts = []

    for i, doc in enumerate(docs, start=1):

        context_parts.append(
            f"""
SOURCE {i}

Title: {doc.get('title', 'Unknown')}

Source: {doc.get('source', 'Unknown')}

Content:
{doc['content']}
"""
        )

    context = "\n\n".join(context_parts)

    return {
        "retrieved_context": context,
        "retrieved_sources": docs
    }