import flet as ft
import time

def import_images(n_images):
    imgs = []

    for i in range(n_images):
        imgs.append(ft.Image(src=f"https://picsum.photos/150/150?{time.time()}", width=180, height= 180))

    return imgs

def main(page: ft.Page):

    def minus_click(e):
        value = int(txt_number.value)
        if value == 1:
            txt_number.value = "1"
        else:
            txt_number.value = str(value-1)

        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    def close_dlg(e):
        dlg.open = False
        page.update()

    products = ft.GridView(expand=True, max_extent=200, child_aspect_ratio=1)
    
    txt_number = ft.TextField(value="1", text_align=ft.TextAlign.RIGHT, width=100)

    dlg = ft.AlertDialog(
        title=ft.Text("Seleccione la cantidad"),
        content=ft.Column(controls=[
            ft.Row([
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click)
            ]),
            ft.Text("Descripción: Coca Cola Zero Calorias"),
            ft.Text("Stock: 12"),
            ft.Text("Importe: $19.99"),
            ft.Text("IVA: $10"),
            ft.Text("Total: $29.99")
        ], height=200),
        actions=[
            ft.TextButton("Agregar al carrito", on_click=close_dlg),
            ft.TextButton("Cancelar", on_click=close_dlg)
        ],
    )

    imgs = import_images(50)

    def menu_change(e):
        if(e.control.selected_index == 0):
            testText.visible = False
            products.visible = True
        if(e.control.selected_index == 1):
            testText.visible = True
            products.visible = False
        page.update()

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
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

    page.appbar = ft.AppBar(
        title=ft.Text("Selección de Productos"),
        bgcolor=ft.colors.INVERSE_PRIMARY

    )

    testText = ft.Text("Estás en el carrito")
    testText.visible = False

    page.add(
        ft.Row([
            rail,
            ft.VerticalDivider(width=1),
            products,
            testText
        ],width=1080, height=720, vertical_alignment=ft.CrossAxisAlignment.START),
    )

    for img in imgs:
        products.controls.append(
            ft.Container(
                img,
                width=100,
                height=100,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_100,
                border=ft.border.all(1, ft.colors.AMBER_400),
                border_radius=ft.border_radius.all(5),
                ink=True,
                on_click=open_dlg
            )
        )

    page.update()

ft.app(target=main)
