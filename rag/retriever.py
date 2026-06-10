from rag.vector_store import collection


def retrieve(query, k=5):

    results = collection.query(
        query_texts=[query],
        n_results=k
    )

    retrieved_docs = []

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    for doc, metadata in zip(documents, metadatas):

        item = {
            "content": doc
        }

        item.update(metadata)

        retrieved_docs.append(item)

    return retrieved_docs