# pymongo - Biblioteca responsável por gerenciar a conexão com o banco.
from pymongo import MongoClient

# Cria o cliente de conexão apontando para o endereço e porta padrão onde o MongoDB está rodando na máquina.
client = MongoClient("mongodb://localhost:27017/")
# Seleciona o banco de dados chamado "escola". Se esse banco não existir, ele será criado automaticamente.
db = client["escola"]
# Seleciona a coleção chamada "estudantes" dentro do banco "escola".
estudantes = db["estudantes"]

# inser_one - Método que insere um único documento (registro) na coleção.
# Os dados são passados em formato de dicionário, que reflete a estrutura de um JSON.
estudantes.insert_one({"nome": "João", "idade": 20})

# find - Método usado para fazer buscas. Sem nenhum filtro dentro dos parênteses ele retorna todos os documentos da coleção.
# O laço 'for' percorre cada documento retornado pela busca.
# OBS: Automaticamente o MongoDB vai adicionar um campo '_id' único para cada registro.
for estudante in estudantes.find():
    print(estudante)