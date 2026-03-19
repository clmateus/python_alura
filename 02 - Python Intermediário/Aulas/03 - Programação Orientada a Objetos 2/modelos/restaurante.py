from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    # __init__ - Método que o Python executa automaticamente no exato momento da criação da instância de um objeto.
    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    # __str__ - Método que define o que o Python irá retornar quando o objeto for chamado.
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self._ativo}'
    
    # @classmethod - Decorator que transforma um método genérico em um método da classe, em vez de um método do objeto.
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | Ativo')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    # @property - Decorator que transforma um método em um atributo inteligente.
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota < 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return ''
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    # def adicionar_bebida_no_cardapio(self, bebida):
    #     self.cardapio.append(bebida)

    # def adicionar_prato_no_cardapio(self, prato):
    #     self.cardapio.append(prato)

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self.nome}\n')

        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)

# restaurante1 = Restaurante('McDonalds', 'Fast Food')
# restaurante1.alternar_estado()
# # restaurante1.nome = "McDonalds"
# # restaurante1.categoria = "Fast Food"
# # restaurante1.ativo = True

# restaurante2 = Restaurante('Burger King', 'Fast Food')
# restaurante2.nome = "Burger King"
# restaurante2.categoria = "Fast Food"
# restaurante2.ativo = False

# dir - Lista todos os atributos de um objeto. Ideal para usar quando não conhecemos a classe.
# print(dir(restaurante1))

# # vars - Cria um dicionário com os atributos de um objeto.
# print(vars(restaurante1))

# print(restaurante1)
# print(restaurante2)

# Restaurante.listar_restaurantes()