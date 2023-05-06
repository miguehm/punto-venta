import flet as ft

def getVistaPagoConsentido():
    total_cobrar_tf = ft.TextField(
        label="Total a cobrar",
        icon=ft.icons.MONEY,
        hint_text="Ingrese el total a cobrar",
        value="64.96",
        read_only=True
    )

    id_consentido_tf = ft.TextField(
        label="ID Cliente Consentido",
        icon=ft.icons.MANAGE_ACCOUNTS,
        hint_text="Ingrese el ID del cliente",
    )

    def confirmacion_pago(e):

        class IdErroneo(Exception):
            def __init__(self, mensaje):
                self.mensaje = mensaje

            def __str__(self):
                return self.mensaje

        try:
            total_cobrar = f"{total_cobrar_tf.value}"
            total_cobrar = round(float(total_cobrar))

            id_consentido = f"{id_consentido_tf.value}"
            
            if len(id_consentido) != 8:
                raise IdErroneo("El formato del ID es incorrecto (8 caracteres)")

            # pendiente
            articulos_vendidos = 3

            def close_confirmacion_dlg(e):
                confirmacion_dlg.open = False
                e.control.page.update()

            confirmacion_dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text("Confirme la compra"),
                content=ft.Column([
                    ft.Text(f"Nombre: Eduardo Hernández Guzman"),
                    ft.Text(f"ID: {id_consentido}"),
                    ft.Text(f"Total crédito asignado: 2000"),
                    ft.Text(f"Total a cobrar: {total_cobrar}"),
                    ft.Text(f"Crédito restante: {2000-total_cobrar}"),
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
        except IdErroneo as err:
            e.control.page.snack_bar = ft.SnackBar(ft.Text(f"{err}"))
            e.control.page.snack_bar.open = True
            e.control.page.update()

    # elementos de pago_efectivo
    pago_consentido = ft.Column([
        total_cobrar_tf,
        id_consentido_tf,
        ft.ElevatedButton(
            text="click",
            on_click=confirmacion_pago
        )
    ])

    return pago_consentido

