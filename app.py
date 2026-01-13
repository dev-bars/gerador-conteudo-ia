import streamlit as st
import google.generativeai as genai

# Minha chave gerada pelo Gemini (aistudio.google.)
minha_chave = "Removi a chave"
genai.configure(api_key=minha_chave)

# Versão que utilizei do Gemini
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("Gerador de Conteúdo Financeiro")

if st.button('Gerar Texto'):
    with st.spinner('Processando...'):
        try:
            #Processamento de dados
            response = model.generate_content("Escreva aproximadamente 200 palavras sobre investimentos e rendimento financeiro.")
            
            # Saída de dados
            st.write(response.text)
            st.success("Concluído!")
            
        except Exception as e:
            st.error(f"Erro: {e}")
