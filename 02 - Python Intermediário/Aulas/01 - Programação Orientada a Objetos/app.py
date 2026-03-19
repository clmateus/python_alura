from modelos.restaurante import Restaurante

restaurante1 = Restaurante('McDonalds', 'Fast Food')
# restaurante2 = Restaurante('Bar do João', 'Brasileira')
# restaurante3 = Restaurante('Si Senõr', 'Mexicana')

restaurante1.alternar_estado()
restaurante1.receber_avaliacao('João', 5)
restaurante1.receber_avaliacao('Maria', 3)
restaurante1.receber_avaliacao('José', 4)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()