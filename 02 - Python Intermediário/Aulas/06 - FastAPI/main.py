# uvicorn - Uvicorn é um servidor web para o Python
# Para usar o Uvicorn, é necessário usar o comando no terminal: 'uvicorn main:app --reload'
# fastapi - Biblioteca que serve para criar APIs
from fastapi import FastAPI, Query
import requests

# Cria o aplicativo principal da API e atribui a variável app
app = FastAPI()

# Diz que a próxima função vai responder no endereço '/api/hello'
@app.get('/api/hello')
# Função que será executada quando acessarem o endereço acima
def hello_world():
    # Retorna a mensagem abaixo em formato de dicionário (JSON)
    return {'Hello':'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados':dados_json}
        
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })
        
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
    else:
        return {'Erro':f'{response.status_code} - {response.text}'}