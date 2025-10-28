import streamlit as st

def configure_interface():
    st.title("Upload de Arquivo DIO Desafio 1 Azure Fake Docs")
    
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        file_name = uploaded_file.name

        # Enviar para o Blob Storage
        # Aqui você chamaria sua função de upload e obteria a URL do blob
        blob_url = upload_to_blob(uploaded_file)  # Exemplo de função fictícia

        # Chamar a função de detecção de informações de cartão de crédito
        credit_card_info = detect_credit_card_info(blob_url)  # Função fictícia

        if blob_url:
            st.write(f"Arquivo {file_name} enviado com sucesso para o Azure Blob Storage")
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Erro ao enviar o arquivo {file_name} para o Azure Blob Storage")

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem enviada", use_column_width=True)
    st.write("Resultado da validação:")

    if credit_card_info and credit_card_info.get("card_name"):
        st.markdown("<h1 style='color: green;'>Cartão Válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do Titular: {credit_card_info.get('card_name')}")
        st.write(f"Banco Emissor: {credit_card_info.get('bank_name')}")
        st.write(f"Data de Validade: {credit_card_info.get('expiry_date')}")
    else:
        st.markdown("<h1 style='color: red;'>Cartão Inválido</h1>", unsafe_allow_html=True)
        st.write("Este não é um cartão de crédito válido.")

if __name__ == "__main__":
    configure_interface()
