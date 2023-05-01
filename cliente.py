from faker import Faker
from faker.providers import credit_card

import subprocess

fake = Faker()
fake.add_provider(credit_card)

numero_tarjeta = fake.credit_card_number()
ccv = fake.credit_card_security_code

output = subprocess.run(["curl", "-s", "https://www.uuidgenerator.net/api/version4"], capture_output=True, text=True)

class Cliente:
    def __init__(self, nombre, is_consentido):
        self.__nombre = nombre
        self.__id = output.stdout[:8]
        self.__is_consentido = is_consentido
        self.__credito = 0
        self.__numero_tarjeta = fake.credit_card_number()
        self.__nip_tarjeta = fake.credit_card_security_code()

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

    def setCredito(self, credito):
        self.__is_consentido = True
        self.__credito = credito

    def print_obj(self):
        for clave, valor in vars(self).items():
            print(f"{clave}: {valor}")

c1 = Cliente("Miguel", False)
c1.print_obj()
c1.setCredito(999)
c1.print_obj()
