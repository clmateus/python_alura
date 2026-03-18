class Restaurante():
    restaurantes = []

    # __init__ - Método que o Python executa automaticamente no exato momento da criação da instância de um objeto.
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = True
        Restaurante.restaurantes.append(self)

    # __str__ - Método que define o que o Python irá retornar quando o objeto for chamado.
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self._ativo}'
    
    def listar_restaurantes():
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | Ativo')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

    # @property - Decorator que transforma um método em um atributo inteligente.
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'

restaurante_1 = Restaurante('McDonalds', 'Fast Food')
# restaurante_1.nome = "McDonalds"
# restaurante_1.categoria = "Fast Food"
# restaurante_1.ativo = True

restaurante_2 = Restaurante('Burger King', 'Fast Food')
# restaurante_2.nome = "Burger King"
# restaurante_2.categoria = "Fast Food"
# restaurante_2.ativo = False

# dir - Lista todos os atributos de um objeto. Ideal para usar quando não conhecemos a classe.
# print(dir(restaurante_1))

# # vars - Cria um dicionário com os atributos de um objeto.
# print(vars(restaurante_1))

# print(restaurante_1)
# print(restaurante_2)

Restaurante.listar_restaurantes()