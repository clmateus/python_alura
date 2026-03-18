def calculadora():
    try:
        numero_1 = float(input("Digite o primeiro número: "))
        operacao = input("Escolha a operação (+, -, *, /): ")
        numero_2 = float(input("Digite o segundo número: "))

        if operacao == "+":
            return numero_1 + numero_2
        elif operacao == "-":
            return numero_1 - numero_2
        elif operacao == "*":
            return numero_1 * numero_2
        elif operacao == "/":
            return numero_1 / numero_2
        else:
            raise ValueError("Opção inválida.")
        
    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")

print(calculadora())