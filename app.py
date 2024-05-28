import streamlit as st
import requests
import json

API_URL = 'http://localhost:8000'

st.title('Frontend de Teste para API Embrapa')

endpoints = {
    '/dados': 'Obter todos os dados',
    '/dados/{arquivo}': 'Obter dados de um arquivo específico',
    '/listar_arquivos': 'Listar arquivos disponíveis'
}

selected_endpoint = st.selectbox('Selecione um endpoint:', list(endpoints.keys()))
st.write(endpoints[selected_endpoint])

if selected_endpoint == '/dados/{arquivo}':
    arquivo = st.text_input('Nome do arquivo:')
else:
    arquivo = None

if st.button('Fazer Requisição'):
    url = f'{API_URL}{selected_endpoint}'
    if arquivo:
        url = url.format(arquivo=arquivo)

    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            st.json(data)
        except json.JSONDecodeError:
            st.text(response.text)
    else:
        st.error(f'Erro na requisição: {response.status_code}')