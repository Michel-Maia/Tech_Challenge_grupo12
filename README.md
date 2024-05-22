# Tech_Challenge_FIAP 
## Grupo12

Tech Challenge é o projeto da fase que englobará os conhecimentos obtidos em todas as disciplinas da fase. Esta é uma atividade que, a princípio, deve ser desenvolvida em grupo. 

#### 🚀 Começando 
<br>

###### O Problema

Você foi contratado(a) para uma consultoria e seu trabalho envolve analisar os dados de vitivinicultura da Embrapa, os quais estão disponíveis (http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01).

A ideia do projeto é a criação de uma API pública de consulta nos dados do site nas respectivas abas:

* Produção
* Processamento
* Comercialização
* Importação
* Exportação

A API vai servir para alimentar uma base de dados que futuramente será usada para um modelo de Machine Learning.

###### Os objetivos incluem:

- Criar uma Rest API em Python que faça a consulta no site da Embrapa.
- A API deve estar documentada.
- É recomendável (não obrigatório) a escolha de um método de autenticação (JWT, por exemplo).
- Criar um plano para fazer o deploy da API, desenhando a arquitetura do projeto desde a ingestão até a alimentação do modelo (aqui não é necessário elaborar um modelo de ML, mas é preciso que vocês escolham um cenário interessante em que a API possa ser utilizada).
- Fazer um MVP realizando o deploy com um link compartilhável e um repositório no github.

#### 🔧 Instalação
Criando o ambiente virtual 

````
python -m venv nome_
````
Instale as dependências 

````
pip install fastapi
````

O uvicorn será usado como servidor

````
pip install uvicorn
````

#### 🛠️ Construído com

Python - Linguagem 
Beautiful Soup - Usado para Webscraping

<br>

#### ✒️ Autores
<br>
Isabelli Andrade de Souza - https://github.com/Isabellitankian
<br>
Lucas Souza Andrade dos Santos - https://github.com/LSouzaAndrade
<br>
Michel de Lima Maia - https://github.com/Michel-Maia
<br>
Valquiria Rodrigues de Oliveira Pires - https://github.com/KyraPires
