from src.rag.config import settings
from langchain_chroma import Chroma
from pathlib import Path
import shutil
from src.rag.embeddings import get_embeddings

def vector_store(chunks):
    ''' Creating the vector store '''

    if Path(settings.PERSIST_DIR).exists():
        shutil.rmtree(settings.PERSIST_DIR)

    vector_store = Chroma(
        persist_directory=settings.PERSIST_DIR,
        collection_name=settings.COLLECTION_NAME,
        embedding_function=get_embeddings()
    )
    vector_store.add_documents(documents=chunks)
    return vector_store


def load_vector_store():
    ''' Loading the vector store '''

    if not Path(settings.PERSIST_DIR).exists():
        raise FileNotFoundError("No vector DB found. Run scripts/ingest.py first")
        
    vector_store = Chroma(
        persist_directory=settings.PERSIST_DIR,
        collection_name=settings.COLLECTION_NAME,
        embedding_function=get_embeddings()
    )
    return vector_store 