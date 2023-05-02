import flet as ft
import csv
from clase_producto import Producto

def main(page: ft.Page):

    productos = []

    with open('archivo.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for i, fila in enumerate(lector_csv):
            if fila[0] == "nombre":
                continue
            productos.append(
                Producto(
                    fila[0],
                    fila[1],
                    fila[2],
                    fila[3],
                    fila[4],
                    fila[5],
                    fila[6],
                    fila[7],
                )
            )

    containers = []
    for i in productos:
        containers.append(i.getContainer())

    vista_productos = ft.Row(controls=
        containers
    )

    page.add(vista_productos)

    page.update()

ft.app(target=main)

