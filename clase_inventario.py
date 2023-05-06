import csv
import copy

from clase_producto import Producto

class Inventario:
    def __init__(self, file):
        self.__productos = [] # : Producto
        self.cargar_productos(file)

    def cargar_productos(self, file):
        # leer ruta del archivo csv y cargarlo al array
        with open(f"{file}", 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                if fila[0] == "nombre":
                    continue
                producto = Producto()
                producto.setNombre(fila[0])
                producto.setTipo(fila[1])
                producto.setId(fila[2])
                producto.setIva(fila[3])
                producto.setDescripcion(fila[4])
                producto.setCantidad(fila[5])
                producto.setPrecio(fila[6])
                producto.setImagen(fila[7])

                self.__productos.append(producto)
                del producto

    def agregar_productos(self, producto):
        self.__productos.append(producto)

    def modificar_producto(self, producto):
        # en base al Id del producto
        # buscarlo en el diccionario y modificarlo
        # el id no se puede modificar una vez se
        # agrega
        for i in range(len(self.__productos)):
            if self.__productos[i].getId() == producto.getId():
                self.__productos[i] = copy.deepcopy(producto)
                break

    def actualizar_inventario(self):
        # actualiza el csv
        pass

    def getProductos(self):
        return self.__productos

    def __str__(self):
        return str(self.__productos[1])

def main():
    inv = Inventario("productos.csv")
    print(inv.getProductos()[1])

    modificado = inv.getProductos()[1]

    modificado.setId("aaaaaaa")
    print(inv.getProductos()[1])

if __name__ == "__main__":
    main()
