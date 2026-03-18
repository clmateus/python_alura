class Restaurante():
    nome = ''
    categoria = ''
    ativo = False

restaurante_1 = Restaurante()
restaurante_1.nome = "McDonalds"
restaurante_1.categoria = "Fast Food"
restaurante_1.ativo = True

restaurante_2 = Restaurante()
restaurante_2.nome = "Burger King"
restaurante_2.categoria = "Fast Food"
restaurante_2.ativo = False

restaurantes = [restaurante_1, restaurante_2]

# dir - Lista todos os atributos de um objeto. Ideal para usar quando não conhecemos a classe.
print(dir(restaurante_1))

# vars - Cria um dicionário com os atributos de um objeto.
print(vars(restaurante_1))