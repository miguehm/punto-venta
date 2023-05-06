import flet as ft
import csv
from clase_producto import Producto
from clase_cliente import Cliente

def main(page: ft.Page):
    page.title = "Stock productos / clientes"
    page.appbar = ft.AppBar(
        title=ft.Text("Stock productos / clientes"),
        bgcolor=ft.colors.INVERSE_PRIMARY

    )

    vistas = []

    # lectura de datos

    productos = []

    with open('productos.csv', 'r') as archivo_csv:
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

    tabla_productos = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Tipo")),
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Descripción")),
            ft.DataColumn(ft.Text("Cantidad")),
            ft.DataColumn(ft.Text("Precio")),
            ft.DataColumn(ft.Text("Imagen")),
            ft.DataColumn(ft.Text("")),
            ],
        rows=[]
        )

    for i in productos:
        tabla_productos.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(i.getNombre())),
                    ft.DataCell(ft.Text(i.getTipo())),
                    ft.DataCell(ft.Text(i.getId())),
                    ft.DataCell(ft.Text(i.getDescripcion())),
                    ft.DataCell(ft.Text(i.getCantidad())),
                    ft.DataCell(ft.Text(i.getPrecio())),
                    ft.DataCell(ft.Text(i.getImagen())),
                    ft.DataCell(i.getModificarBtn()),
                    ]
                )
        )

    def show_agregar_producto(e):
        def cerrar_dlg(e):
            dlg_agregar_producto.open = False
            e.control.page.update()

        dlg_agregar_producto = ft.AlertDialog(
            title=ft.Text("Nuevo Cliente"),
            content=ft.Column([
                ft.TextField(
                    label="Nombre: ",
                    value=f""
                ),
                ft.TextField(
                    label="Tipo: ",
                    value=f""
                ),
                ft.TextField(
                    label="Descripción: ",
                    value=f""
                ),
                ft.TextField(
                    label="Cantidad: ",
                    value=f""
                ),
                ft.TextField(
                    label="Precio: ",
                    value=f""
                ),
                ft.TextField(
                    label="Imagen: ",
                    value=f""
                ),
            ]),
            actions=[
                ft.TextButton("Agregar", on_click=cerrar_dlg),
                ft.TextButton("Cancelar", on_click=cerrar_dlg),
                    ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        e.control.page.dialog = dlg_agregar_producto
        dlg_agregar_producto.open = True
        e.control.page.update()

    vista_inventario = ft.Column([
            tabla_productos,
            ft.ElevatedButton("Agregar Producto", on_click=show_agregar_producto)
        ], alignment=ft.MainAxisAlignment.START, expand=True)
    vista_inventario.visible = True
    vistas.append(vista_inventario)

    # Vista Clientes

    tabla_clientes = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Consentido")),
            ft.DataColumn(ft.Text("Credito")),
            ft.DataColumn(ft.Text("Tarjeta")),
            ft.DataColumn(ft.Text("Nip")),
            ft.DataColumn(ft.Text("")),
            ],
        rows=[]
        )

    clientes = []

    ## Borrar ##
    c1 = Cliente("Eduardo Hernandez Guzman", True, 2000)
    c1.setId("3e52a3a6")
    c1.setCredito("1935")
    c1.setNumeroTarjeta("4950497487039935")
    c1.setNipTarjeta("495")

    clientes.append(c1)

    for i in clientes:
        tabla_clientes.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(i.getNombre())),
                    ft.DataCell(ft.Text(i.getId())),
                    ft.DataCell(ft.Text(i.getIsConsentido())),
                    ft.DataCell(ft.Text(i.getCredito())),
                    ft.DataCell(ft.Text(i.getNumeroTarjeta())),
                    ft.DataCell(ft.Text(i.getNipTarjeta())),
                    ft.DataCell(i.getModificarBtn()), # boton
                    ]
                )
        )

    def show_agregar_cliente(e):
        dlg_agregar_cliente = ft.AlertDialog(
            title=ft.Text("Nuevo Cliente"),
            content=ft.Column([
                ft.TextField(
                    label="Nombre: ",
                ),
                ft.TextField(
                    label="Credito: ",
                    value=f""
                ),
            ])   
        )

        e.control.page.dialog = dlg_agregar_cliente
        dlg_agregar_cliente.open = True
        e.control.page.update()

    vista_clientes = ft.Column([
            tabla_clientes,
            ft.ElevatedButton("Agregar Cliente", on_click=show_agregar_cliente)
        ], alignment=ft.MainAxisAlignment.START, expand=True)
    vista_clientes.visible = False
    vistas.append(vista_clientes)

    def show_inventario(e):
        vista_inventario.visible = True
        vista_clientes.visible = False
        page.update()

    def show_clientes(e):
        vista_inventario.visible = False
        vista_clientes.visible = True
        page.update()

    def select_opc(e):
        if(e.control.selected_index == 0):
            show_inventario(e)
            page.update()
        else:
            show_clientes(e)
    
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.INVENTORY_2_OUTLINED),
                selected_icon_content=ft.Icon(ft.icons.INVENTORY),
                label="Inventario"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.PERSON_2_OUTLINED),
                selected_icon_content=ft.Icon(ft.icons.PERSON_2_ROUNDED),
                label="Clientes"
            ),
        ],
        on_change=select_opc
    )

    page.add(ft.Row(
        [
            rail,
            ft.VerticalDivider(width=1),
            vista_inventario,
            vista_clientes
        ],
        width=1920,
        height=700
    ))

    page.update()

ft.app(target=main)
