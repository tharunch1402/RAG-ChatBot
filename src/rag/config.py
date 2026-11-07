import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    # Api_key & Model 
    OPENAI_API_KEY  = os.getenv("OPENAI_API_KEY")
    MODEL = 'gpt-4o-mini'

    # Embeddings
    embedding_model = 'text-embedding-3-small'


settings = Settings()
