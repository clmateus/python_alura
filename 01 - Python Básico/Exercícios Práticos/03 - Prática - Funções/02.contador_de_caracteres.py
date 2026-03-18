def contador_de_caracteres(palavra):
    return len(palavra)

palavra = input("Digite uma palavra: ")
quantidade_de_caracteres = contador_de_caracteres(palavra)

print(f"Essa palavra tem {quantidade_de_caracteres} caracteres")