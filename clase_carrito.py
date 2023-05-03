from clase_producto import Producto

class Carrito:
    def __init__(self):
        self.__productos = {}

    def addProducto(self, objProducto, cantidad):
        try:
            id_producto = objProducto.getId()
            print(id_producto)
            if id_producto in self.__productos:
                self.__productos[id_producto] += int(cantidad)
            else:
                self.__productos[id_producto] = int(cantidad)

        except ValueError:
            print("no se ingresó un numero")

    def getCarrito(self):
        return self.__productos

def main():
    c = Carrito()

    c.addProducto(Producto("xd", "xd", "1291htht", "16", "Hola", "8", "77", "image"), "9")
    c.addProducto(Producto("xd", "xd", "1291htht", "16", "Hola", "8", "77", "image"), "2")

if __name__ == "__main__":
    main()
