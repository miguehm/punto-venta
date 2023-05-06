import flet as ft
import time

from flet_core import row
import clase_cliente
from vista_pago_efectivo import getVistaPagoEfectivo
from vista_pago_tarjeta import getVistaPagoTarjeta
from vista_pago_consentido import getVistaPagoConsentido
from vista_productos import getVistaProductos
import os
import glob

def main(page: ft.Page):
    # ------- Config gral pagina -----------
    page.appbar = ft.AppBar(
        title=ft.Text("Selección de Productos"),
        bgcolor=ft.colors.INVERSE_PRIMARY

    )
    # --------------------------------------

    # ---------- Menu Lateral ----------
    def menu_change(e):
        if(e.control.selected_index == 0):
            vista_carrito.visible = False
            vista_pago_efectivo.visible = False
            vista_productos.visible = True
            vista_pago_tarjeta.visible = False
            vista_pago_consentido.visible = False
            e.page.appbar.title = ft.Text("Selección de productos")
        if(e.control.selected_index == 1):
            e.page.appbar.title = ft.Text("Carrito")
            vista_carrito.visible = True
            vista_pago_efectivo.visible = False
            vista_productos.visible = False
            vista_pago_tarjeta.visible = False
            vista_pago_consentido.visible = False
        page.update()

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME_OUTLINED,
                selected_icon=ft.icons.HOME_FILLED,
                label="Productos"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SHOPPING_CART_OUTLINED,
                selected_icon=ft.icons.SHOPPING_CART_ROUNDED,
                label="Carrito"
            ),
        ],
        on_change=menu_change,
    )
    # ----------------------------------

    def show_vista_pago_efectivo(e):
        dlg_metodo_pago.open = False
        e.control.page.update()

        vista_pago_efectivo.visible = True
        vista_carrito.visible = False
        vista_productos.visible = False
        vista_pago_consentido.visible = False
        e.page.appbar.title = ft.Text("Pago en Efectivo")
        page.update()

    def show_vista_pago_tarjeta(e):
        dlg_metodo_pago.open = False
        e.control.page.update()

        vista_pago_efectivo.visible = False
        vista_carrito.visible = False
        vista_productos.visible = False
        vista_pago_consentido.visible = False
        vista_pago_tarjeta.visible = True
        e.page.appbar.title = ft.Text("Pago con Tarjeta")
        page.update()

    def show_vista_pago_consentido(e):
        dlg_metodo_pago.open = False
        e.control.page.update()

        vista_pago_efectivo.visible = False
        vista_carrito.visible = False
        vista_productos.visible = False
        vista_pago_tarjeta.visible = False
        vista_pago_consentido.visible = True
        e.page.appbar.title = ft.Text("Pago con Tarjeta")
        page.update()

    dlg_metodo_pago = ft.AlertDialog(
        title=ft.Text("Seleccione el método de pago"),
        content=ft.Column([
            ft.ElevatedButton("Efectivo", on_click=show_vista_pago_efectivo),
            ft.ElevatedButton("Pago con Tarjeta", on_click=show_vista_pago_tarjeta),
            ft.ElevatedButton("Crédito Cliente Consentido", on_click=show_vista_pago_consentido),
        ], height=145)
    )

    def show_dlg_metodo_pago(e):
        e.control.page.dialog = dlg_metodo_pago
        dlg_metodo_pago.open = True
        e.control.page.update()

    # ----------- Vista carrito ---------------
    vista_carrito = ft.Column(controls=[
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Producto")),
                ft.DataColumn(ft.Text("Cantidad"))
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Aceite")),
                        ft.DataCell(ft.Text("2")),
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Arroz")),
                        ft.DataCell(ft.Text("1")),
                    ]
                ),
            ]
        ),
        ft.ElevatedButton("Continuar compra", on_click=show_dlg_metodo_pago),
    ])
    vista_carrito.visible = False

    # importando vista pago efectivo
    vista_pago_efectivo = getVistaPagoEfectivo()
    vista_pago_efectivo.visible = False

    vista_pago_tarjeta = getVistaPagoTarjeta()
    vista_pago_tarjeta.visible = False

    vista_pago_consentido = getVistaPagoConsentido()
    vista_pago_consentido.visible = False

    # -----------------------------------------

    # ----------- Vista productos -------------
    vista_productos = getVistaProductos()
    # -----------------------------------------

    # ------- Agregar vistas a la pagina ------
    page.add(
        ft.Row([
            rail,
            ft.VerticalDivider(width=1),
            vista_productos,
            vista_carrito,
            vista_pago_efectivo,
            vista_pago_tarjeta,
            vista_pago_consentido
        ],
        width=1080,
        height=720,
        vertical_alignment=ft.CrossAxisAlignment.START),
    )
    # -----------------------------------------

    page.update()

ft.app(target=main)
