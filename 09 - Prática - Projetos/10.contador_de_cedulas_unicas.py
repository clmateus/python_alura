def entrada_saque():
    try:
        valor_do_saque = float(input("Digite o valor do saque: "))
        
        if valor_do_saque % 2 != 0:
            print(f"Erro: O valor deve ser múltiplo de 2.")
            input(f"Pressione uma tecla para voltar.")
            valor_do_saque = 0
            entrada_saque()

        return valor_do_saque
    
    except:
        print(f"Erro: Digite um número válido.")

def calcula_celulas():
    valor_do_saque = entrada_saque()

    cedulas = [100, 50, 20, 10, 5, 2]

    for cedula in cedulas:
        quantidade = valor_do_saque // cedula
        if quantidade > 0:
            print(f"{quantidade} cédulas de R$ {cedula}")
            valor_do_saque = valor_do_saque % cedula

calcula_celulas()