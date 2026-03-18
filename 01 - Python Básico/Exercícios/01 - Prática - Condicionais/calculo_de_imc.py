try:
    peso = float(input("Digite o seu peso (kg): "))
    altura = float(input("Digite a sua altura (m): "))

    imc = peso / (altura ** 2)
    print(f"Seu IMC é: {imc:.2f}")

    if imc < 18.5:
        print("Você está abaixo do peso.")
    elif imc < 25:
        print("Você está com peso normal.")
    else:
        print("Você está acima do peso")
except:
    print("Erro! Digite um número válido.")