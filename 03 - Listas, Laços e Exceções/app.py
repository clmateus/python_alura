import os

restaurantes = ["Pizzaria", "Hamburgueria"]

def exibir_nome_do_programa():
    print("Restaurant Manager\n")
    
def finalizar_app():
    exibir_subtitulo("Encerrando o programa.")

def voltar_ao_menu_principal():
    input("\nDigite qualquer tecla para voltar ao menu principal.")
    main()

def exibir_subtitulo(subtitulo):
    os.system("cls")
    print(f"{subtitulo}\n")

def opcao_invalida():
    print("Opção inválida")
    voltar_ao_menu_principal()

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante a ser cadastrado: ")
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Lista de restaurantes cadastrados")
    for restaurante in restaurantes:
        print(restaurante)
    voltar_ao_menu_principal()

def escolher_opcao():

    try:
        opcao_escolhida = int(input("Digite a opção desejada: "))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print("Ativar restaurante")
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()
    
def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()