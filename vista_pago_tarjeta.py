import flet as ft

def getVistaPagoEfectivo():
    # Pago en Efectivo

    total_cobrar_tf = ft.TextField(
        label="Total a cobrar",
        icon=ft.icons.MONEY,
        hint_text="Ingrese el total a cobrar",
    )

    numero_tarjeta_tf = ft.TextField(
        label="Numero de tarjeta",
        icon=ft.icons.MONEY_OFF_OUTLINED,
        hint_text="Ingrese su numero de tarjeta a 16 dígitos",
    )

    numero_pin_tf = ft.TextField(
        label="PIN",
        icon=ft.icons.MONEY_OFF_OUTLINED,
        hint_text="Ingrese su codigo de seguridad",
        password=True,
        can_reveal_password=True
    )

    def confirmacion_pago(e):

        class DatoIncorrecto(Exception):
            def __init__(self, mensaje):
                self.mensaje = mensaje

            def __str__(self):
                return self.mensaje

        try:
            total_cobrar = f"{total_cobrar_tf.value}"
            total_cobrar = int(total_cobrar)

            numero_tarjeta = f"{numero_tarjeta_tf.value}"

            numero_pin = f"{numero_pin_tf.value}"
            
            if len(numero_tarjeta) < 16 or len(numero_tarjeta) > 16:
                raise DatoIncorrecto("Formato incorrecto en el numero de tarjeta")

            if len(numero_pin) < 3 or len(numero_pin) > 3:
                raise DatoIncorrecto("Formato incorrecto en el numero PIN")

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
                    ft.Text(f"Total articulos vendidos: {articulos_vendidos}"),
                ], height=300),
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
            e.control.page.snack_bar = ft.SnackBar(ft.Text("Ingrese datos validos"))
            e.control.page.snack_bar.open = True
            e.control.page.update()
        except DatoIncorrecto as err:
            e.control.page.snack_bar = ft.SnackBar(ft.Text(f"{err}"))
            e.control.page.snack_bar.open = True
            e.control.page.update()

    # elementos de pago_efectivo
    pago_efectivo = ft.Column([
        total_cobrar_tf,
        numero_tarjeta_tf,
        numero_pin_tf,
        ft.ElevatedButton(
            text="Continuar",
            on_click=confirmacion_pago
        )
    ])

    return pago_efectivo

def main(page: ft.Page):
    vista = getVistaPagoEfectivo()
    page.add(vista)

    page.update()

if __name__ == "__main__":
    #main()
    ft.app(target=main)
