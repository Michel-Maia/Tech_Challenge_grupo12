import csv
import requests

resposta = {}
urlBase = "http://vitibrasil.cnpuv.embrapa.br/download/"
arquivos = ["Producao", "ProcessaViniferas", "ProcessaAmericanas", "ProcessaMesa", "ProcessaSemclass", "Comercio", "ImpVinhos", 
            "ImpEspumantes", "ImpFrescas", "ImpPassas", "ImpSuco", "ExpVinho", "ExpEspumantes", "ExpUva", "ExpSuco"]

for arquivo in arquivos:
    url = f"{urlBase}{arquivo}.csv"
    response = requests.get(url)
    if response.status_code != 200:
        resposta = {'erro': response.status_code}
        break
    reader = csv.DictReader(response.text.splitlines())
    resposta[arquivo] = []
    for linha in reader:
        resposta[arquivo].append(linha)

print(resposta)