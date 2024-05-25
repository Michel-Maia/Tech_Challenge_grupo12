import utils.embrapa
from fastapi import FastAPI

api = FastAPI()

@api.get('/dados')
def dados_arquivos():
    return utils.embrapa.request()

@api.get('/dados/{arquivo:str}')
def dados_arquivo(arquivo:str):
    return utils.embrapa.request(arquivo)

@api.get('/listar_arquivos')
def listar_arquivos():
    return {'arquivos': utils.embrapa.arquivos}