import os

tarefas = []

def adicionar_tarefa():
    os.system("cls")
    tarefas.append(input("Digite a tarefa: "))
    print(f"Tarefa adicionada!")
    voltar_ao_menu_principal()

def visualizar_tarefas():
    os.system("cls")

    numero_tarefa = 1

    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for i in tarefas:
            print(f"{numero_tarefa}. {i}")
            numero_tarefa += 1

    voltar_ao_menu_principal()

def remover_tarefa():
    os.system("cls")

    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        try:
            indice_tarefa = int(input("Digite o número da tarefa a ser removida: ")) - 1
            print(f"Tarefa {tarefas[indice_tarefa]} removida!")
            tarefas.pop(indice_tarefa)
        except ValueError:
            print("Erro! Digite um número válido para remover")
        except IndexError:
            print("Erro! Essa tarefa não existe.")
        
    voltar_ao_menu_principal()
    

def voltar_ao_menu_principal():
    input("Digite qualquer tecla para voltar ao menu principal")
    main()

def encerrar_app():
    os.system("cls")
    print(f"Saindo do gerenciador de tarefas. Até mais!")

def mostrar_menu():
    print(f"Bem-vindo ao gerenciador de tarefas!\n")
    print(f"1. Adicionar tarefa")
    print(f"2. Visualizar tarefas")
    print(f"3. Remover tarefa")
    print(f"4. Sair")

def escolha_menu():
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        adicionar_tarefa()
    elif escolha == "2":
        visualizar_tarefas()
    elif escolha == "3":
        remover_tarefa()
    elif escolha == "4":
        encerrar_app()
    else:
        print("Erro: Opção inválida! Escolha uma opção entre 1 e 4")
        voltar_ao_menu_principal()

def main():
    os.system("cls")
    mostrar_menu()
    escolha_menu()

if __name__ == "__main__":
    main()