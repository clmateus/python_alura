def retorna_idade(ano_nascimento, ano_atual):
    return ano_nascimento - ano_atual

try:
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    ano_atual = int(input("Digite o ano atual: "))
    idade = retorna_idade(ano_nascimento, ano_atual)

    print(f"A idade é {idade} anos")
except:
    print("Erro! Digite um ano válido.")