try:
    temperatura = float(input("Digite a temperatura atual: "))

    if temperatura <= 25:
        pass
    else:
        print("Alerta! Temperatura acima do limite permitido.")
except:
    print("Erro! Digite uma temperatura válida.")