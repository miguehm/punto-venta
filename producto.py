class Producto:
    def __init__(self, nombre, tipo, id, iva, descripcion, cantidad, precio, imagen):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__id = id
        self.__iva = iva
        self.__descripcion = descripcion
        self.__cantidad = cantidad
        self.__precio = precio
        self.__imagen = imagen

    def getNombre(self):
        return self.__nombre

    def getTipo(self):
        return self.__tipo

    def getId(self):
        return self.__id

    def getIva(self):
        return self.__iva

    def getDescripcion(self):
        return self.__descripcion

    def getCantidad(self):
        return self.__cantidad

    def getPrecio(self):
        return self.__precio

    def getImagen(self):
        return self.__imagen
