import csv
from io import open_code
import flet as ft
from flet_core import image
import subprocess

class Producto:
    def __init__(self,
            nombre="",
            tipo="",
            id=subprocess.run(["curl", "-s", "https://www.uuidgenerator.net/api/version4"], capture_output=True, text=True).stdout[:8],
            iva="",
            descripcion="",
            cantidad="",
            precio="",
            imagen=""):
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
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setTipo(self, tipo):
        self.__tipo = tipo

    def setId(self, id):
        self.__id = id

    def setIva(self, iva):
        self.__iva = iva

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def setCantidad(self, cantidad):
        self.__cantidad = cantidad

    def setPrecio(self, precio):
        self.__precio = precio

    def setImagen(self, imagen):
        self.__imagen = imagen

    def getContainer(self):

        cantidad = ft.TextField(value="1", text_align=ft.TextAlign.RIGHT, width=100)
        self.__iva = f"{round(int(self.__precio)*0.16, 2)}"

        # ------------ Dialogo Info ------------
        def minus_click(e):
            value = int(cantidad.value)
            if value == 1:
                cantidad.value = "1"
            else:
                cantidad.value = str(value-1)

            e.page.update()

        def plus_click(e):
            cantidad.value = str(int(cantidad.value) + 1)
            e.page.update()

        def open_dlg(e):
            print(e)
            e.page.dialog = info
            info.open = True
            e.page.update()

        def close_dlg(e):
            info.open = False
            e.page.update()

        info = ft.AlertDialog(
            title=ft.Text("Seleccione la cantidad"),
            content=ft.Column(controls=[
                ft.Row([
                    ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                    cantidad,
                    ft.IconButton(ft.icons.ADD, on_click=plus_click)
                ]),
                ft.Text(f"Nombre: {self.__nombre}"),
                ft.Text(f"Tipo: {self.__tipo}"),
                ft.Text(f"ID: {self.__id}"),
                ft.Text(f"IVA: {self.__iva}"),
                ft.Text(f"Descripción: {self.__descripcion}"),
                ft.Text(f"Stock: {self.__cantidad}"),
                ft.Text(f"Precio: {float(self.__precio)+float(self.__iva)}"),
            ], height=300),
            actions=[
                ft.TextButton("Agregar al carrito", on_click=close_dlg),
                ft.TextButton("Cancelar", on_click=close_dlg)
            ],
        )
        # --------------------------------------

        container = ft.Container(
            content=ft.Image(self.getImagen()),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.GREEN_200,
            width=150,
            height=150,
            on_click=open_dlg
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

    def getModificarBtn(self):
        
        def guardar_cambio(e):
            dialogo.open = False
            e.control.page.update()

        def dlg_edit_producto(e):

            e.control.page.dialog = dialogo
            dialogo.open = True
            e.control.page.update()

        dialogo = ft.AlertDialog(
            title=ft.Text("Modificando Producto"),
            content=ft.Column([
                ft.TextField(
                    label="Nombre: ",
                    value=f"{self.getNombre()}"
                ),
                ft.TextField(
                    label="Tipo: ",
                    value=f"{self.getTipo()}"
                ),
                ft.TextField(
                    label="ID: ",
                    value=f"{self.getId()}",
                    read_only=True
                ),
                ft.TextField(
                    label="Descripción: ",
                    value=f"{self.getDescripcion()}"
                ),
                ft.TextField(
                    label="Cantidad: ",
                    value=f"{self.getCantidad()}"
                ),
                ft.TextField(
                    label="Precio: ",
                    value=f"{self.getPrecio()}"
                ),
                ft.TextField(
                    label="Imagen: ",
                    value=f"{self.getImagen()}"
                ),
            ]),
            actions=[
                ft.TextButton("Guardar", on_click=guardar_cambio),
                ft.TextButton("Cancelar"),
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )

        btn = ft.IconButton(
            icon=ft.icons.EDIT,
            on_click=dlg_edit_producto
        )

        return btn


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
            )
            productos.append(producto)
    
    return productos

def main():
    #productos = leer_productos()

    #for i in productos:
    #    print(i.getNombre())

    producto = Producto()
    producto.setNombre("Papel Higienico")
    print(producto)

if __name__ == "__main__":
    main()
