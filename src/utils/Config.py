import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    # Endpoint e chave do Azure Document Intelligence
    DOCUMENT_INTELLIGENCE_ENDPOINT = os.getenv("ENDPOINT")
    DOCUMENT_INTELLIGENCE_KEY = os.getenv("SUBSCRIPTION_KEY")
    
    # Configurações do Azure Blob Storage
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    CONTAINER_NAME = os.getenv("CONTAINER_NAME")
