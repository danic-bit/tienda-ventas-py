
"""En un archivo producto.py, definir la clase que permita instanciar productos.
Considera para la definición de esta clase lo señalado en la descripción de la
problemática (utilice ENCAPSULAMIENTO)."""

"""Los productos tienen un nombre, un precio y un stock. Los 3 valores se deben
solicitar al momento de crear un producto nuevo, pero si no se indica stock, se
asume que es 0. No se puede modificar el nombre ni el precio de un producto, solo
su stock. Si se intenta modificar el stock por un valor menor a 0, se debe asignar 0 en
su lugar. De cada producto se puede obtener su nombre, su precio o su stock."""

class Producto():
    def __init__(self, nombre: str, precio: int, stock : int = 0 ):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock if stock >= 0 else self.__stock

#sehacen los 3 getters porque todos los valores se pueden consultar, pero el setter solo se hace a stock (el unico que puede cambiar)
    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    #setter de stock:
    @stock.setter
    def stock (self, stock):
        self.__stock = stock if stock >= 0 else self.__stock #el nuevo valor de stock también va con la validación y esto quiere decir que si es 0 queda en 0, pero si es negativo, queda en 0


    #a continuación Sobrecargaas de métodos predeterminados de python:

    def __eq__(self, other):
        return self.__nombre.lower() == other.nombre.lower() #devuelve self, es decir, todo el objeto, incluido su nombre, y el stock (que es lo único que cambia)

    def __iadd__(self, other):
        if self == other:
            self.__stock += other.stock
        return self

    def __isub__(self, other):
        if self == other:
            self.__stock -= other.stock
        return self

    """ sobrecargar el método __iadd__ (permite
sobrecargar operación de asignación +=), de forma que, al sumar dos instancias
iguales del producto, se añada al stock de la instancia actual el stock de la
segunda instancia. El método debe retornar la instancia actual """

if __name__ == "__main__":
    p01=Producto("pollo", 3500, 2)
    print(p01)
    print(p01.stock)