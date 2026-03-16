import os

restaurantes = [{"nome": "Restaurante1", "categoria": "Pizzaria", "ativo": True},
                {"nome": "Restaurante2", "categoria": "Sushi", "ativo": False}]

def exibir_nome_do_programa():
    """Essa função é responsável por escrever o nome da aplicação no menu principal"""

    print("Restaurant Manager\n")
    
def finalizar_app():
    """Essa função é responsável por encerrar a aplicação"""

    exibir_subtitulo("Encerrando o programa.")

def voltar_ao_menu_principal():
    """Essa função é responsável por retornar o usuário ao menu principal"""

    input("\nDigite qualquer tecla para voltar ao menu principal.")
    main()

def exibir_subtitulo(subtitulo):
    """Essa função é responsável por escrever os subtítulos dos menus da aplicação"""

    os.system("cls")
    linha = "*" * len(subtitulo) 
    print(linha)
    print(f"{subtitulo}")
    print(linha)

def opcao_invalida():
    """Essa função é responsável por retornar o usuário ao menu principal caso ele digite uma opção inexistente"""

    print("Opção inválida")
    voltar_ao_menu_principal()

def exibir_opcoes():
    """Essa função é responsável por criar um menu visual para o usuário"""

    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alternar estado de restaurante")
    print("4. Sair\n")

def cadastrar_novo_restaurante():
    """Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria do restaurante
    
    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    
    """

    exibir_subtitulo("Cadastro de novos restaurantes")

    nome_do_restaurante = input("Digite o nome do restaurante a ser cadastrado: ")
    categoria_do_restaurante = input(f"Digite a categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome": nome_do_restaurante, "categoria": categoria_do_restaurante, "ativo": False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()

def listar_restaurantes():
    """Essa função é responsável por listar os restaurantes cadastrados"""

    exibir_subtitulo("Lista de restaurantes cadastrados")

    print(f'{"Nome do restaurante".ljust(20)} | {"Categoria".ljust(20)} | Estado')
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado"
        print(f"{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")
    voltar_ao_menu_principal()

def alterar_estado_restaurante():
    """Essa opção é responsável por ativar ou desativar o estado de um restaurante cadastrado
    
    Inputs:
    - Nome do restaurante

    Outputs:
    - Alterna o estado do restaurante entre ativo (True) e desativado (False)
    
    """

    exibir_subtitulo("Alteração de estado dos restaurantes cadastrados")

    nome_restaurante = input("Digite o nome do restaurante que você deseja alterar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso!" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso!"
            print(mensagem)

    if not restaurante_encontrado:
        print(f"O restaurante {nome_restaurante} não foi encontrado.")

    voltar_ao_menu_principal()

def escolher_opcao():
    """Essa função é responsável por captar a opção desejada pelo usuário e chamar a função correspondente"""

    try:
        opcao_escolhida = int(input("Digite a opção desejada: "))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alterar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()
    
def main():
    """Essa função é a função principal que é executada no início da aplicação"""

    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()