import utils.embrapa
from fastapi import FastAPI

app = FastAPI()

@app.get('/dados')
def dados_arquivos():
    return utils.embrapa.request()

@app.get('/dados/{arquivo:str}')
def dados_arquivo(arquivo:str):
    return utils.embrapa.request(arquivo)

@app.get('/listar_arquivos')
def listar_arquivos():
    return {'arquivos': utils.embrapa.arquivos}