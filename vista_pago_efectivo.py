import flet as ft

def main(page: ft.Page):
    # Pago en Efectivo

    total_cobrar_tf = ft.TextField(
        label="Total a cobrar",
        icon=ft.icons.MONEY,
        hint_text="Ingrese el total a cobrar",
    )

    pago_cantidad_tf = ft.TextField(
        label="Pago en cantidad",
        icon=ft.icons.MONEY,
        hint_text="Ingrese el pago recibido",
    )

    def confirmacion_pago(e):

        class CobroErroneo(Exception):
            def __init__(self, mensaje):
                self.mensaje = mensaje

            def __str__(self):
                return self.mensaje

        try:
            total_cobrar = f"{total_cobrar_tf.value}"
            total_cobrar = int(total_cobrar)

            pago_cantidad = f"{pago_cantidad_tf.value}"
            pago_cantidad = int(pago_cantidad)
            
            if pago_cantidad < total_cobrar:
                raise CobroErroneo("El pago es menor al cobro total")

            cambio = pago_cantidad - total_cobrar

            # pendiente
            articulos_vendidos = -1

            def close_confirmacion_dlg(e):
                confirmacion_dlg.open = False
                e.control.page.update()

            confirmacion_dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text("Confirme la compra"),
                content=ft.Column([
                    ft.Text(f"Total a cobrar: {total_cobrar}"),
                    ft.Text(f"Pago en cantidad: {pago_cantidad}"),
                    ft.Text(f"Cambio: {cambio}"),
                    ft.Text(f"Total articulos vendidos: {articulos_vendidos}"),
                ], height=400),
                actions=[
                    ft.TextButton("Aceptar", on_click=close_confirmacion_dlg),
                    ft.TextButton("Cancelar", on_click=close_confirmacion_dlg),
                ]
            )

            # abriendo dialogo de confirmacion
            e.control.page.dialog = confirmacion_dlg
            confirmacion_dlg.open = True
            e.control.page.update()

        except ValueError:
            e.control.page.snack_bar = ft.SnackBar(ft.Text("Ingrese cantidades validas"))
            e.control.page.snack_bar.open = True
            e.control.page.update()
        except CobroErroneo as err:
            e.control.page.snack_bar = ft.SnackBar(ft.Text(f"{err}"))
            e.control.page.snack_bar.open = True
            e.control.page.update()

    # elementos de pago_efectivo
    pago_efectivo = ft.Column([
        total_cobrar_tf,
        pago_cantidad_tf,
        ft.ElevatedButton(
            text="click",
            on_click=confirmacion_pago
        )
    ])

    page.add(
        pago_efectivo
    )

    page.update()

ft.app(target=main)
