import random

def pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]

    escolha = input(f"Escolha: pedra, papel ou tesoura? ").lower()
    escolha_computador = random.choice(opcoes)

    if escolha not in opcoes:
        print("Escolha inválida!")
        return 

    print(f"Computador escolheu: {escolha_computador}")

    if escolha == escolha_computador:
        print(f"Computador escolheu: {escolha_computador}")
        print(f"Empate!")
    elif (
        (escolha == "pedra" and escolha_computador == "tesoura") or
        (escolha == "tesoura" and escolha_computador == "papel") or
        (escolha == "papel" and escolha_computador == "pedra")
    ):
        print("Você venceu!")
    else:
        print("Você perdeu!") 

pedra_papel_tesoura()