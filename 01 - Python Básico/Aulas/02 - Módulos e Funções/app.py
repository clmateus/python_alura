import os

def exibir_nome_do_programa():
    print("Restaurant Manager\n")
    
def finalizar_app():
    os.system('cls') # windows
    # os.system('clear') macOS
    print("Encerrando o programa.")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def escolher_opcao():
    opcao_escolhida = int(input("Digite a opção desejada: "))

    # Escolha de opções com if/elif/else
    # if opcao_escolhida == "1":
    #     print("Cadastrar restaurante")
    # elif opcao_escolhida == "2":
    #     print("Listar restaurantes")
    # elif opcao_escolhida == "3":
    #     print("Ativar restaurante")
    # else:
    #     finalizar_app()

    # Escolha de opções com match
    match opcao_escolhida:
        case 1:
            print("Cadastrar restaurante")
        case 2:
            print("Listar restaurantes")
        case 3:
            print("Ativar restaurante")
        case 4:
            finalizar_app()
        case _:
            print("Opção inválida")

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()