import random

def gerar_senha():
    caracteres = "abcdefghijklmnopqrstuvwxyz"
    caracteres_maiusculos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digitos = "1234567890"
    caracteres_especiais = "!@#$%&*"

    senha = [
        random.choice(caracteres),
        random.choice(caracteres_maiusculos),
        random.choice(digitos),
        random.choice(caracteres_especiais)
    ]

    todos_caracteres = caracteres + caracteres_maiusculos + digitos + caracteres_especiais

    # extend - método que adiciona todos os itens de um elemento iterável ao final da lista
    senha.extend(random.choices(todos_caracteres, k=8))

    # shuffle - método da biblioteca random que embaralha os itens de uma lista
    random.shuffle(senha)

    # join - método para strings que une elementos de uma lista e transforma-os em uma única string, usando um separador que você define
    # "separador".join(lista)
    return "".join(senha)

print(f"Senha gerada: {gerar_senha()}")