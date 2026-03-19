from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante1 = Restaurante('McDonalds', 'Fast Food')
bebida1 = Bebida('Suco de Melancia', 5.00, 'Grande')
prato1 = Prato('Bife com Fritas', 20, 'Arroz, feijão, contra-filé e fritas')

def main():
    print(bebida1)
    print(prato1)

if __name__ == '__main__':
    main()