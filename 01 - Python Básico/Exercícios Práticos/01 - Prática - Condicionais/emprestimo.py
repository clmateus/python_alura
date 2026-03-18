try:
    renda_mensal = float(input("Digite o valor da sua renda mensal: "))
    parcela_desejada = float(input("Digite o valor da parcela desejada: "))

    if renda_mensal > 2000:
        if parcela_desejada > (renda_mensal * 0.3):
            print("Empréstimo negado: parcela acima de 30% da renda.")
        else:
            print("Empréstimo aprovado.")
    else:
        print("Empréstimo negado: renda mensal precisa ser maior que R$ 2000,00")
    
except:
    print("Erro! Digite um valor em R$.")