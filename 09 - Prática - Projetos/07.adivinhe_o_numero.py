import random

def numero_aleatorio():
    escolha_do_computador = random.randint(1, 100)
    tentativas = 0

    try:
        escolha_do_usuario = int(input(f"Tente adivinhar o número (1-100): "))

        while True:
            if not 1 <= escolha_do_usuario <= 100:
                raise ValueError("Número fora do intervalo! Digite um número entre 1 e 100.")

            tentativas += 1

            if escolha_do_usuario == escolha_do_computador:
                print(f"Parabéns você acertou o número {escolha_do_computador}")
                print(f"Tentativas: {tentativas}")
                break
            else:
                if escolha_do_usuario > escolha_do_computador:
                    escolha_do_usuario = int(input("Muito alto! Tente novamente: "))
                else:
                    escolha_do_usuario = int(input("Muito baixo! Tente novamente: "))

    except ValueError as e:
        print(f"Entrada inválida: {e}")

numero_aleatorio()