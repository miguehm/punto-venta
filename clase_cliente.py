from faker import Faker
from faker.providers import credit_card
import subprocess
import flet as ft

from flet_core.icons import QR_CODE
from clase_carrito import Carrito

# Gen num tarjeta
fake = Faker()
fake.add_provider(credit_card)

class Cliente:
    def __init__(self, nombre, is_consentido, credito):
        self.__nombre = nombre
        self.__id = subprocess.run(["curl", "-s", "https://www.uuidgenerator.net/api/version4"], capture_output=True, text=True).stdout[:8]
        self.__is_consentido = is_consentido
        self.__credito = credito
        self.__numero_tarjeta = fake.credit_card_number()
        self.__nip_tarjeta = fake.credit_card_security_code()
        self.__carrito = Carrito()

    def getNombre(self):
        return self.__nombre

    def getId(self):
        return self.__id

    def getIsConsentido(self):
        return self.__is_consentido

    def getCredito(self):
        return self.__credito

    def getNumeroTarjeta(self):
        return self.__numero_tarjeta

    def getNipTarjeta(self):
        return self.__nip_tarjeta

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setId(self, id):
        self.__id = id

    def setIsConsentido(self, id):
        self.__is_consentido = id

    def setNumeroTarjeta(self, numero_tarjeta):
        self.__numero_tarjeta = numero_tarjeta

    def setNipTarjeta(self, nip_tarjeta):
        self.__nip_tarjeta = nip_tarjeta

    def setCredito(self, credito):
        self.__is_consentido = True
        self.__credito = credito

    def print_obj(self):
        for clave, valor in vars(self).items():
            print(f"{clave}: {valor}")

    def addProducto(self, objProducto, cantidad):
        self.__carrito.addProducto(objProducto, cantidad)

    def getCarrito(self):
        return self.__carrito.getCarrito()

    def getModificarBtn(self):
        
        def guardar_cambio(e):
            dialogo.open = False
            e.control.page.update()

        def dlg_edit_producto(e):

            e.control.page.dialog = dialogo
            dialogo.open = True
            e.control.page.update()

        dialogo = ft.AlertDialog(
            title=ft.Text("Modificando Cliente"),
            content=ft.Column([
                ft.TextField(
                    label="Nombre: ",
                    value=f"{self.getNombre()}"
                ),
                ft.TextField(
                    label="ID: ",
                    value=f"{self.getId()}",
                    read_only=True
                ),
                ft.TextField(
                    label="Consentido: ",
                    value=f"{self.getIsConsentido()}"
                ),
                ft.TextField(
                    label="Credito: ",
                    value=f"{self.getCredito()}"
                ),
                ft.TextField(
                    label="Tarjeta: ",
                    value=f"{self.getNumeroTarjeta()}"
                ),
                ft.TextField(
                    label="Nip: ",
                    value=f"{self.getNipTarjeta()}"
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


def main():
    c1 = Cliente("Miguel", False, 0)
    c2 = Cliente("Marco", 1, 9232)
    c1.print_obj()
    c2.print_obj()
    c1.setCredito(999)
    c1.print_obj()

if __name__ == "__main__":
    main()
