import csv
import requests
import streamlit as st
import matplotlib.pyplot as plt
from fastapi import FastAPI

class Crawler:

    def request_embrapa(arquivo = None):
        urlBase = 'http://vitibrasil.cnpuv.embrapa.br/download/'
        arquivos = ['Producao', 'ProcessaViniferas', 'ProcessaAmericanas', 'ProcessaMesa', 'ProcessaSemclass', 'Comercio', 'ImpVinhos', 
                    'ImpEspumantes', 'ImpFrescas', 'ImpPassas', 'ImpSuco', 'ExpVinho', 'ExpEspumantes', 'ExpUva', 'ExpSuco']   
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

op = Crawler()


def main():

    
    st.set_page_config(
    page_title="Olá! O intutito desse request é fazer o download no site da embrapa e realizar o download dos CSVs que são de importância para nós.",
    page_icon="👋",
    )

    st.write("# Olá! 👋👋👋 Bem vindo ao demonstrativo do site da Embrapa, no qual fazemos o request de suas APIs!")

    st.sidebar.success("Estamos em obras aqui, peço que espere um pouquinho.")

    st.markdown(
        """
        - Site da Emprapa:  http://vitibrasil.cnpuv.embrapa.br

        - Contém os dados da produção:  http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02

        - Contém os dados do processamento:  http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03

        - Contém os dados da comercialização:  http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04

        - Contém os dados da importação: http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05

        - Contém os dados da Exportação:  http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06
        
    """
    )


if __name__ == '__main__':
  
    main()

    

app = FastAPI()

@app.get('/')
def get_todos_arquivos():
    return request_embrapa()

@app.get('/{arquivo:str}')
def get_arquivo(arquivo:str):
    return request_embrapa(arquivo)

