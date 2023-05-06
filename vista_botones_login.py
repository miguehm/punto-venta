import flet as ft

def main(page: ft.Page): # define funcion main (page)

    def credencialEncargado(e):
        dialog = ft.AlertDialog(
            title=ft.Text("Ingrese sus credenciales"),
            content=ft.Column([
                ft.TextField(
                    label="Usuario",
                    hint_text="Ingrese su usuario",
                    prefix_icon=ft.icons.SUPERVISOR_ACCOUNT,
                ),
                ft.TextField(
                    label="Contraseña",
                    hint_text="Ingrese su contraseña",
                    prefix_icon=ft.icons.PASSWORD,
                    password=True,
                    can_reveal_password=True
                ),
            ], height=150),
            actions=[
                ft.TextButton("Ingresar")
            ]
        )

        e.control.page.dialog = dialog
        dialog.open = True
        e.control.page.update()


    loginEncargado = ft.Container(
        content=ft.Text("Entrar como ENCARGADO"),
        on_click=credencialEncargado,
        width=200,
        height=50,
        bgcolor=ft.colors.BLUE_GREY_400,
        border_radius=10,
        alignment=ft.alignment.center
    )

    loginDuenio = ft.Container(
        content=ft.Text("Entrar como DUEÑO"),
        on_click=credencialEncargado,
        width=200,
        height=50,
        bgcolor=ft.colors.BLUE_GREY_400,
        border_radius=10,
        alignment=ft.alignment.center
    )

    page.add(ft.Column([
            ft.Text("Punto de Venta", size=20),
            ft.Row([
                loginEncargado,
                loginDuenio
            ], alignment=ft.MainAxisAlignment.CENTER,
            spacing=50)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER)
    )

    page.update()

ft.app(target=main)
