# uvicorn - Uvicorn é um servidor web para o Python
# Para usar o Uvicorn, é necessário usar o comando no terminal: 'uvicorn main:app --reload'
# fastapi - Biblioteca que serve para criar APIs
from fastapi import FastAPI

# Cria o aplicativo principal da API e atribui a variável app
app = FastAPI()

# Diz que a próxima função vai responder no endereço '/api/hello'
@app.get('/api/hello')
# Função que será executada quando acessarem o endereço acima
def hello_world():
    # Retorna a mensagem abaixo em formato de dicionário (JSON)
    return {'Hello':'World'}