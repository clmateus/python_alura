try:
    hora = float(input("Digite a hora atual (formato 24 horas): "))

    if (hora < 8 or hora > 18):
        print("Acesso negado.")
    else:
        print("Acesso permitido.")
except:
    print("Erro! Digite um horário válido.")