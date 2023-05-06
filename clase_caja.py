class Caja:
    def __init__(self):
        self.__dinero_actual = 0

    def agregar_diner(self, cantidad):
        self.__dinero_actual += cantidad

    def cortar_caja(self):
        print(f"Corte actual: {self.__dinero_actual}")
        self.__dinero_actual = 0
