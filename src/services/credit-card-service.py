from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentAnalysisClient
from azure.ai.documentintelligence.models import AnalyzeResult
from utils.Config import Config

def analyze_credit_card(card_url):
    try:
        # Criar cliente do Azure Document Intelligence
        client = DocumentAnalysisClient(
            endpoint=Config.DOCUMENT_INTELLIGENCE_ENDPOINT,
            credential=AzureKeyCredential(Config.DOCUMENT_INTELLIGENCE_KEY)
        )

        # Iniciar análise usando o modelo predefinido de cartão de crédito
        poller = client.begin_analyze_document(
            model_id="prebuilt-creditCard",
            document_url=card_url
        )
        result = poller.result()

        # Extrair informações do cartão
        card_info = {}
        for document in result.documents:
            fields = document.fields
            card_info = {
                "card_name": fields.get("CardHolderName").value if fields.get("CardHolderName") else None,
                "card_number": fields.get("CardNumber").value if fields.get("CardNumber") else None,
                "expiry_date": fields.get("ExpirationDate").value if fields.get("ExpirationDate") else None,
                "bank_name": fields.get("Issuer").value if fields.get("Issuer") else None
            }
        return card_info

    except Exception as e:
        print(f"Erro ao analisar o cartão de crédito: {e}")
        return None
