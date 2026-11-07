from langchain_text_splitters import RecursiveCharacterTextSplitter
from rag.config import settings

def text_splitter(documents):
    ''' Converting the documents into chunks '''

    chunks = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )
    return chunks.split_documents(documents)
    