import csv
import flet as ft

class Producto:
    def __init__(self, nombre, tipo, id, iva, descripcion, cantidad, precio, imagen):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__id = id
        self.__iva = iva
        self.__descripcion = descripcion
        self.__cantidad = cantidad
        self.__precio = precio
        self.__imagen = imagen

    def getNombre(self):
        return self.__nombre

    def getTipo(self):
        return self.__tipo

    def getId(self):
        return self.__id

    def getIva(self):
        return self.__iva

    def getDescripcion(self):
        return self.__descripcion

    def getCantidad(self):
        return self.__cantidad

    def getPrecio(self):
        return self.__precio

    def getImagen(self):
        return self.__imagen

    def getContainer(self):
        container = ft.Container(
            content=ft.Image(self.getImagen()),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.GREEN_200,
            width=150,
            height=150,
            on_click=lambda e: print(f"{self}")
        )
        return container

    def __str__(self):
        r = f"Nombre: {self.getNombre()}\n"
        r = f"{r}{self.getTipo()}\n"
        r = f"{r}{self.getId()}\n"
        r = f"{r}{self.getIva()}\n"
        r = f"{r}{self.getDescripcion()}\n"
        r = f"{r}{self.getCantidad()}\n"
        r = f"{r}{self.getPrecio()}\n"
        r = f"{r}{self.getImagen()}\n"
        return r


def leer_productos():
    productos = []
    with open('productos.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for i in lector_csv:
            if i[0] == "nombre":
                continue

            producto = Producto(
                i[0],
                i[1],
                i[2],
                i[3],
                i[4],
                i[5],
                i[6],
                i[7],
                1 # pos
            )
            productos.append(producto)
    
    return productos

def main():
    productos = leer_productos()

    for i in productos:
        print(i.getNombre())

if __name__ == "__main__":
    main()
