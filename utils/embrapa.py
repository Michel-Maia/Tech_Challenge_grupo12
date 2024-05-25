import csv
import requests

arquivos = ['Producao', 'ProcessaViniferas', 'ProcessaAmericanas', 'ProcessaMesa', 'ProcessaSemclass', 'Comercio', 'ImpVinhos', 
            'ImpEspumantes', 'ImpFrescas', 'ImpPassas', 'ImpSuco', 'ExpVinho', 'ExpEspumantes', 'ExpUva', 'ExpSuco']   

def request(arquivo = None):
    urlBase = 'http://vitibrasil.cnpuv.embrapa.br/download/'
    resposta = {}
    if arquivo == None:
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
    elif arquivo in arquivos:
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