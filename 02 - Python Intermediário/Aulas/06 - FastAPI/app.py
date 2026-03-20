# requests - Biblioteca usada para se comunicar com a internet
import requests
# json - Biblioteca usara para manipulação de arquivos e dados no formato JSON
import json

# API com dados de alguns restaurantes
url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

# Método 'GET' - Método que busca e guarda os dados de um endereço específico
# O método 'GET' sempre irá retornar um código de acordo com o resultado da busca. Veja alguns exemplos:
# 200 - Sucesso
# 301 - Redirecionamento
# 401 - Não autorizado
# 404 - Não encontrado
response = requests.get(url)

print(response)

# Verifica se a requisição foi processada com sucesso (código 200)
if response.status_code == 200:
    # Converte os dados recebidos da API para uma lista de dicionários
    dados_json = response.json()

    # Dicionário vazio para agrupar os itens por nome do restaurante
    dados_restaurante = {}
    # Laço para percorrer cada item que veio da API
    for item in dados_json:
        # Armazena o nome do restaurante atual
        nome_do_restaurante = item['Company']
        
        # Verifica se o restaurante ainda não existe no dicionário dados_restaurante
        if nome_do_restaurante not in dados_restaurante:
            # Cria uma lista vazia associada a esse restaurante
            dados_restaurante[nome_do_restaurante] = []

        # Adiciona os detalhes de cada item do cardapio de cada restaurante
        dados_restaurante[nome_do_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })
else:
    # Caso a requisição tenha falhado, exibe o código de erro no console
    print(f'O erro foi: {response.status_code}')

# Laço para percorrer o dicionário final, separando o nome do restaurante e seus itens
for nome_do_restaurante, dados in dados_restaurante.items():
    # Define o nome do arquivo que será salvo, usando o nome do respectivo restaurante e a extensão .json
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, mode='w', encoding='utf8') as fp:
        # dump - Método da biblioteca json que permite inserir informações dentro de um arquivo
        # O dump recebe 3 parâmetros:
        # 1 - A informação a ser inserida
        # 2 - O arquivo que receberá as informações
        # 3 - (opcional) indent - Quantidade de recuo em cada nível de texto
        json.dump(dados, fp, indent=4)