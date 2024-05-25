import streamlit as st
import requests
import json

API_URL = 'http://localhost:8000'
endpoints = {
    '/dados': 'Obter os dados de todos arquivos',
    '/dados/{arquivo}': 'Obter os dados de um arquivo específico',
    '/listar_arquivos': 'Listar arquivos disponíveis'
}

st.title('Frontend de teste para API Embrapa')
endpointSelecionado = st.selectbox('Selecione um endpoint:', list(endpoints.keys()))
st.write(endpoints[endpointSelecionado])

if endpointSelecionado == '/dados/{arquivo}':
    arquivo = st.text_input('Nome do arquivo:')
else:
    arquivo = None

if st.button('Fazer requisição'):
    url = f'{API_URL}{endpointSelecionado}'
    if arquivo:
        url = url.format(arquivo=arquivo)
    response = requests.get(url)
    if response.status_code == 200:
        conteudoCSV = response.json()
        st.json(conteudoCSV)
    else:
        st.error(f'Erro na requisição: {response.status_code}')