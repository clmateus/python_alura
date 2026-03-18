# Exercícios
# 1 - Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
class Carro():
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro1 = Carro('corsa', 'prata', 2006)

# 2 - Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
# 3 - Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
# 4 - Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
class Restaurante():
    def __init__(self, nome, categoria, localizacao, rating, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.localizacao = localizacao
        self.rating = rating

    def __str__(self):
        return f'Restaurante: {self.nome} | Categoria {self.categoria}'
    
mcdonalds = Restaurante('McDonalds', 'Fast Food', 'Centro', 3)

print(mcdonalds)

# 5 - Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
class Cliente():
    def __init__(self, nome, documento, idade, endereco):
        self.nome = nome
        self.documento = documento
        self.idade = idade
        self.endereco = endereco

cliente1 = Cliente('José da Silva', 123, 20, 'Rua 1')
cliente2 = Cliente('Maria de Souza', 456, 25, 'Rua 2')
cliente3 = Cliente('João dos Santos', 789, 30, 'Rua 3')
