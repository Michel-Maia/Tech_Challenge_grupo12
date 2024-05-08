import csv
import requests
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def request_embrapa_geral():
    resposta = {}
    urlBase = 'http://vitibrasil.cnpuv.embrapa.br/download/'
    arquivos = ['Producao', 'ProcessaViniferas', 'ProcessaAmericanas', 'ProcessaMesa', 'ProcessaSemclass', 'Comercio', 'ImpVinhos', 
                'ImpEspumantes', 'ImpFrescas', 'ImpPassas', 'ImpSuco', 'ExpVinho', 'ExpEspumantes', 'ExpUva', 'ExpSuco']

    for arquivo in arquivos:
        url = f'{urlBase}{arquivo}.csv'
        response = requests.get(url)
        if response.status_code != 200:
            resposta = {'erro': response.status_code}
            break
        reader = csv.DictReader(response.text.splitlines())
        resposta[arquivo] = []
        for linha in reader:
            resposta[arquivo].append(linha)
    return resposta

@app.get('/{arquivo:str}')
def request_embrapa_especifico(arquivo: str):
    resposta = {}
    urlBase = 'http://vitibrasil.cnpuv.embrapa.br/download/'
    arquivos = ['Producao', 'ProcessaViniferas', 'ProcessaAmericanas', 'ProcessaMesa', 'ProcessaSemclass', 'Comercio', 'ImpVinhos', 
                'ImpEspumantes', 'ImpFrescas', 'ImpPassas', 'ImpSuco', 'ExpVinho', 'ExpEspumantes', 'ExpUva', 'ExpSuco']

    if arquivo in arquivos:
        url = f'{urlBase}{arquivo}.csv'
        response = requests.get(url)
        if response.status_code != 200:
            resposta = {'erro': response.status_code}
        else:
            reader = csv.DictReader(response.text.splitlines())
            resposta[arquivo] = []
            for linha in reader:
                resposta[arquivo].append(linha)
    else:
        resposta = {'erro': 404}
    return resposta