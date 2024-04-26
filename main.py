from fastapi import FastAPI
import os
import requests
from bs4 import BeautifulSoup

# uvicorn main:app --reload

app = FastAPI()


@app.get("/")
def home():
    return {"teste"}
                         
def identificar_opcoes():
    try:
        response = requests.get('http://vitibrasil.cnpuv.embrapa.br/index.php')
        response.raise_for_status()
        opcoes = {}
        soup = BeautifulSoup(response.text, 'html.parser')
        tabela = soup.find('table', class_='tb_layout no_print')
        botoesOpt = tabela.find_all('button', class_='btn_opt')
        for botaoOpt in botoesOpt:
            valor = botaoOpt.get('value')
            texto = botaoOpt.get_text(strip=True)
            opcoes[texto] = valor
        return opcoes
    except:
        return {'status':'Erro ao prospectar pÃ¡ginas'}


def identificar_subopcoes(opcoes):
    if 'status' in opcoes:
        return opcoes
    subopcoesPorPagina = {}
    for texto, valor in opcoes.items():
        url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao={valor}'
        try:
            response = requests.get(url)
            response.raise_for_status()
            subopcoes = {}
            soup = BeautifulSoup(response.text, 'html.parser')
            botoesSubopt = soup.find_all('button', class_='btn_sopt')
            for botaoSubopt in botoesSubopt:
                textoBotaoSubopt = botaoSubopt.get_text(strip=True)
                valorBotaoSubopt = botaoSubopt.get('value')
                subopcoes[textoBotaoSubopt] = valorBotaoSubopt
            subopcoesPorPagina[valor] = subopcoes
        except:
            return {'status': 'Erro ao prospectar abas'}
    return subopcoesPorPagina


def baixar_csv(subopcoes):
    if 'status' in subopcoes:
        return subopcoes
    try:
        for opt in subopcoes.keys():
            subopts = subopcoes[opt]
            if subopts:
                for subopt, valor in subopts.items():
                    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao={valor}&opcao={opt}'
                    response = requests.get(url)
                    response.raise_for_status()
                    soup = BeautifulSoup(response.text, 'html.parser')
                    link = soup.find('a', class_='footer_content', href=True)
                    if link['href'].endswith('.csv'):
                        csvURL = 'http://vitibrasil.cnpuv.embrapa.br/'+link['href']
                        print(csvURL)
                        response = requests.get(csvURL)
                        nomeDoCSV = os.path.basename(csvURL)
                        with open(nomeDoCSV, 'wb') as file:
                            file.write(response.content)
            else:
                url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao={opt}'
                response = requests.get(url)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, 'html.parser')
                link = soup.find('a', class_='footer_content', href=True)
                if link['href'].endswith('.csv'):
                    csvURL = 'http://vitibrasil.cnpuv.embrapa.br/'+link['href']
                    print(csvURL)
                    response = requests.get(csvURL)
                    nomeDoCSV = os.path.basename(csvURL)
                    with open(nomeDoCSV, 'wb') as file:
                        file.write(response.content)
        return {'status':'Arquivos baixados com sucesso'}
    except:
        return {'status': 'Erro ao baixar CSV'}


opcoesEncontradas = identificar_opcoes()
print(opcoesEncontradas)
subopcoesEncontradas = identificar_subopcoes(opcoesEncontradas)
print(subopcoesEncontradas)
status = baixar_csv(subopcoesEncontradas)
print(status['status'])