from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante1 = Restaurante('McDonalds', 'Fast Food')
bebida1 = Bebida('Suco de Melancia', 5.00, 'Grande')
prato1 = Prato('Bife com Fritas', 20, 'Arroz, feijão, contra-filé e fritas')

restaurante1.adicionar_no_cardapio(bebida1)
restaurante1.adicionar_no_cardapio(prato1)

def main():
    restaurante1.exibir_cardapio

if __name__ == '__main__':
    main()