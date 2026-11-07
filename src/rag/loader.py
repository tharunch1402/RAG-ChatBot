from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

def loading_documents(file_path:str):
    ''' Loading the PDF Files '''

    data_path = Path(file_path)

    if not data_path.exists():
        raise FileNotFoundError(f"The {file_path} is not exist")

    if data_path.suffix.lower() != '.pdf':
        raise ValueError(f'The {file_path} is not pdf format')

    loader = PyPDFLoader(str(data_path))
    documents = loader.load()

    return documents