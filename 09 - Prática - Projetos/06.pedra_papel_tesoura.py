import random

opcoes = ["pedra", "papel", "tesoura"]

escolha = input(f"Escolha: pedra, papel ou tesoura? ").lower()
escolha_computador = random.choice(opcoes)

print(f"Computador escolheu: {escolha_computador}")

if escolha == escolha_computador:
    print(f"Computador escolheu: {escolha_computador}")
    print(f"Empate!")
elif (
    (escolha == "pedra" and escolha_computador == "tesoura")
    (escolha == "tesoura" and escolha_computador == "papel")
    (escolha == "papel" and escolha_computador == "pedra")
):
    print("Você venceu!")
else:
    print("Você perdeu!") 