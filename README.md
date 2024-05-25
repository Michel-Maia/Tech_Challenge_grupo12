# Tech Challenge FIAP - Grupo 12 - Fase 1

## 🚀 Sobre o projeto 

### Escopo:

Analisar os dados de vitivinicultura da Embrapa, os quais estão disponíveis em http://vitibrasil.cnpuv.embrapa.br/index.php.

A ideia do projeto é a criação de uma API pública de consulta nos dados do site nas respectivas abas:

* Produção
* Processamento
* Comercialização
* Importação
* Exportação

A API vai servir para alimentar uma base de dados que futuramente será usada para alimentar um modelo de Machine Learning.

### Objetivos da fase 1:

- Criar uma Rest API em Python que faça a consulta no site da Embrapa.
- A API deve estar documentada.
- É recomendável (não obrigatório) a escolha de um método de autenticação (JWT, por exemplo).
- Criar um plano para fazer o deploy da API, desenhando a arquitetura do projeto desde a ingestão até a alimentação do modelo (aqui não é necessário elaborar um modelo de ML, mas é preciso que vocês escolham um cenário interessante em que a API possa ser utilizada).
- Fazer um MVP realizando o deploy com um link compartilhável e um repositório no github.

## 📋 Pré-requisitos

- Interpretador Python para execução dos códigos;
- Biblioteca FastAPI para criação da API;
- Biblioteca Uvicorn para criação de servidor da API.
- Biblioteca Streamlit para criação de interface de requisições da API.

## 🔧 Instalação
Criação do ambiente virtual:

````
python -m venv nome
````
Instalação das dependências:

````
pip install fastapi
pip install uvicorn
pip install streamlit
````
Para execução tanto do servidor Uvicorn da API, quanto da interface Streamlit, abra dois terminais no diretório base do projeto e execute os seguintes comandos:


- Terminal 1:
````
uvicorn main:api
````
- Terminal 2:
````
streamlit run app.py
````

## ✒️ Autores

Isabelli Andrade de Souza - https://github.com/Isabellitankian
<br>
Lucas Souza Andrade dos Santos - https://github.com/LSouzaAndrade
<br>
Michel de Lima Maia - https://github.com/Michel-Maia
<br>
Valquiria Rodrigues de Oliveira Pires - https://github.com/KyraPires
