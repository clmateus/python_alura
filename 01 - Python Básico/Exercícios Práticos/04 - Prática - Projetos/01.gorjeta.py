def calcula_gorjeta(valor_total, porcentagem_gorjeta):
    return valor_total * (porcentagem_gorjeta / 100)

valor_total = float(input("Digite o valor da conta: "))
porcentagem_gorjeta = float(input("Digite a porcentagem de gorjeta: "))
valor_gorjeta = calcula_gorjeta(valor_total, porcentagem_gorjeta)

print(f"O valor da gorjeta é R$: {valor_gorjeta:.2f}")
print(f"Total a pagar: R$ {valor_total + valor_gorjeta:.2f}")