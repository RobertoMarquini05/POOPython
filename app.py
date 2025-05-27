from Models.restaurante import Restaurante

restaurante_praca = Restaurante("praça", "Gourmet")

restaurante_praca.receber_avaliacao("Roberto", 3)
restaurante_praca.receber_avaliacao("Luma", 5)
restaurante_praca.receber_avaliacao("Lucca", 4)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()