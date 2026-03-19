from modelos.restaurante import Restaurante

restaurante1 = Restaurante('McDonalds', 'Fast Food')
restaurante2 = Restaurante('Bar do João', 'Brasileira')
restaurante3 = Restaurante('Si Senõr', 'Mexicana')

restaurante1.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()