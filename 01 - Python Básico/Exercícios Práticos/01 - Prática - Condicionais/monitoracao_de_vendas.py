try:
    macas = int(input("Digite a quantidade de maçãs vendidas: "))
    bananas = int(input("Digite a quantidade de bananas vendidas: "))

    if macas > bananas:
        print("As maçãs tiveram mais vendas.")
    elif macas < bananas:
        print("As bananas tiveram mais vendas.")
    else:
        print("As vendas de maçãs e bananas empataram.")
except ValueError:
    print("Erro! É necessário inserir um número inteiro.")