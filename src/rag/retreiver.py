from src.rag.vector_stores import load_vector_store
from src.rag.config import settings

def get_retriever():
    """Returns the retreiver"""

    vector_store = load_vectorstore()
    return vector_store.as_retriever(search_kwargs={"k": settings.TOP_K})
