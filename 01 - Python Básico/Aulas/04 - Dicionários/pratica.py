# Exercícios
# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
pessoa = {"nome": "João", "idade": 20, "cidade": "São Paulo"}

print(pessoa)

# 2 - Utilizando o dicionário criado no item 1:
# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.
pessoa["nome"] = "Maria"
pessoa["profissão"] = "Dev"
del pessoa["cidade"]

print(pessoa)

# 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
numeros_e_quadrados = { x: x**2 for x in range(1, 6)}

print(numeros_e_quadrados)

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
dicionario = {"chave1": "valor1", "chave2": "valor2"}

print(f"{'chave1' in dicionario}")
print(f"{'chave3' in dicionario}")

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
frase = "Essa frase é uma string"
contagem_de_palavras = {}
palavras = frase.split()

for palavra in palavras:
    contagem_de_palavras[palavra] = contagem_de_palavras.get(palavra, 0) + 1

print(contagem_de_palavras)