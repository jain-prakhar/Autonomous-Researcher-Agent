import chromadb
import uuid

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="research_documents"
)


def store_documents(documents):

    ids = []
    texts = []
    metadatas = []

    for doc in documents:

        ids.append(str(uuid.uuid4()))

        texts.append(doc["content"])

        metadata = {}
        for key, value in doc.items():
            if key != "content":
                metadata[key] = str(value)
        metadatas.append(metadata)

    collection.add(
        ids=ids,
        documents=texts,
        metadatas=metadatas
    )