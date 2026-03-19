# Listas
# Uma lista é uma coleção de dados mutável.
lista = [1, 2, 8, 5.5]
print(lista[1]) # 2 - Extrai o primeiro elemento
print(lista[0]) # 1 - Extrai o segundo elemento
print(lista[-1]) # 5.5 - Extrai o último elemento
print(lista[0:2]) # [1, 2] - Extrai os elementos do índice 0 até o índice 1 (não inclui o 2) e os coloca em outra lista
print(20 in lista) # False - Verifica se o dado fornecido está presente na lista

# Métodos para listas
lista.append(6) # Adiciona um elemento ao final da lista
print(lista)
lista.insert(0, 2) # Adiciona um elemento em um índice específico (índice, valor)
print(lista)
lista.remove(2) # Remove o primeiro elemento encontrado com o valor especificado
print(lista) 
lista.sort() # Reordena os elementos da lista em ordem crescente. Obs: Só funciona se todos os elementos forem números
print(lista)
lista.reverse() # Reverte a ordem dos elementos da lista
print(lista)
print(lista.pop()) # Remove e retorna o elemento no índice indicado. Se não especificado o índice, remove o último elemento da lista
print(lista)

# Tuplas
# Uma tupla é uma coleção de dados imutável.
tupla = (1, 2, 8, 5.5)
print(tupla[1]) # 2 - Extrai o primeiro elemento
print(tupla[0]) # 1 - Extrai o segundo elemento
print(tupla[-1]) # 5.5 - Extrai o último elemento
print(tupla[0:2]) # (1, 2) - Extrai os elementos do índice 0 até o índice 1 (não inclui o 2) e os coloca em outra tupla
print(20 in tupla) # False - Verifica se o dado fornecido está presente na tupla

# Concatenação de tuplas
# Apesar de imutáveis, podemos criar novas tuplas com base em tuplas já existentes
nova_tupla = tupla + (30, 25, 30)
print(nova_tupla)

# Iteração sobre elementos
# Tanto listas quanto tuplas podem ser iteradas usando laços de repetição
for item in lista:
    print(f'Lista: {item}')

for item in tupla:
    print(f'Tupla: {item}')

# Desempacotamento
# Desempacotamento é uma técnica que permite atribuir os valores de uma lista ou tupla a variáveis de forma mais prática
a, b, c, d = lista
print(a, b, c, d) # 8, 6, 5.5, 2
w, x , y, z = tupla
print(w, x, y, z) # 1, 2, 8, 5.5