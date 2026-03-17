try:
    distancia = float(input("Digite a distância percorrida (em km): "))

    if distancia > 200:
        preco = 30
    elif distancia > 100:
        preco = 20
    else:
        preco = 10

    print(f"Valor do pedágio: R${preco},00")

except:
    print("Erro! Digite um número válido.")