def verifica_numeros(lista_de_numeros):
    for i in lista_de_numeros:
        if type(i) == str:
            return False
        return True

def converte_strings_para_inteiros(string):
    return int(string)

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 
telefones_convertidos = []

for i in telefones:
    telefones_convertidos.append(converte_strings_para_inteiros(i))

if verifica_numeros(telefones_convertidos):
    print("Todos os números foram convertidos corretamente!")
else:
    print("Os números não foram convertidos corretamente")