# json - Biblioteca que contém ferramentas para manipulação de arquivos .json
import json

with open('dados.json', mode='w', encoding='utf8') as fp:
    # dump - Método para inserir dados em um arquivo json
    json.dump({'nome': 'Maria', 'idade': 20, 'enderecos': ['a', 'b']}, fp)