# Exercícios
# 1 - Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.
lista_de_numeros_de_1_a_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_com_quatro_nomes = ["João", "Maria", "José", "Pedro"]
lista_de_anos = [2000, 2026]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
for numero in lista_de_numeros_de_1_a_10:
    print(numero)

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma = 0

for numero in lista_de_numeros_de_1_a_10:
    if numero % 2 == 0:
        pass
    else:
        soma = soma + numero

print(soma)

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
for i in range(10, 0, -1):
    print(i)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{i} x {numero} = {i*numero}")

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
soma = 0

try:
    for numero in lista_de_numeros_de_1_a_10:
        soma = soma + numero
except Exception as e: 
    print(f"Erro! {e}")

print(soma)

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
lista_de_valores = [None, 5, 5, 10]
soma = 0

try:
    for numero in lista_de_valores:
        soma = soma + numero
    media = soma / len(lista_de_valores)
    print(f"A média dos valores fornecidos é: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Erro! {e}")