# Exercícios
# 1 - Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
class Restaurante():
    nome = ''
    categoria = ''
    ativo = True

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Restaurante Praça'
restaurante_praca.categoria = 'Italiana'

# 2 - Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
print(restaurante_praca.nome)

# 3 - Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
if restaurante_praca.ativo:
    print(f"O {restaurante_praca.nome} está ativo")
else:
    print(f"O {restaurante_praca.nome} está inativo")

# 4 - Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
categoria = Restaurante.categoria

# 5 - Altere o valor do atributo nome para 'Bistrô'.
restaurante_praca.categoria = "Bistrô"
print(restaurante_praca.categoria)

# 6 - Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

# 7 - Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
if restaurante_pizza.categoria == 'Fast Food':
    print(f'É Fast Food.')
else:
    print(f'Não é Fast Food')

# 8 - Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True

# 9 - Imprima no console o nome e a categoria da instância restaurante_praca.
print(f"Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}")