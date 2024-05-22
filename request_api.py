from fastapi import FastAPI
import requests


app = FastAPI()

@app.get("/producao")
def obter_dados_externos():
    url_producao = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'
    url_processamento = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_03'
    url_comercializacao = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04'
    url_importacao = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05'
    url_exportacao = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06'

    urls = ['url_producao', 'url_processamento', 'url_comercializacao', 'url_importacao', 'url_exportacao']

    #Send a GET request to the API endpoint
    array=[]
    for url in urls:
        response = requests.get(url)
        data = response.json()
        array.append(data)

    if response.status_code == 200:
        return response.json()
    else:
        return {"erro": "Não foi possível obter os dados da API externa"}

