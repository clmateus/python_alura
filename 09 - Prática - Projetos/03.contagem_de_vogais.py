def conta_vogais(frase):
    vogais = "aeiou"
    contador = 0

    for i in frase.lower():
        if i in vogais:
            contador += 1
    
    return contador

print(conta_vogais("aabcde"))