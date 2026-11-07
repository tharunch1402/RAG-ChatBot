from src.rag.config import settings
from langchain_openai import OpenAIEmbeddings

def get_embeddings():
    ''' Getting the embeddings from the OpenAI API '''

    embeddings = OpenAIEmbeddings(
        model=settings.embedding_model,
        openai_api_key=settings.OPENAI_API_KEY
    )
    return embeddings