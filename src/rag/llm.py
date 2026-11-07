from src.rag.config import settings
from langchain_openai import ChatOpenAI

def get_llm():
    ''' Getting the LLM from the OpenAI API '''

    if not settings.OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY not found. Check your .env file")

    llm = ChatOpenAI(
        model=settings.LLM_MODEL,
        openai_api_key=settings.OPENAI_API_KEY,
        temperature=settings.TEMPERATURE,
    )
    return llm