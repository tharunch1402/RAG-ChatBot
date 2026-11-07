import logging

from src.rag.loader import load_documents
from src.rag.splitter import text_splitter
from rag.vector_store import vector_stores

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s"
)


def main():
    documents = load_documents("data")
    print("Pages loaded:", len(documents))

    chunks = text_splitter(documents)
    print("Chunks created:", len(chunks))

    vector_stores(chunks)
    print("Stored in Chroma ✅")


if __name__ == "__main__":
    main()
