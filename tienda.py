from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):

    def __init__(self, nombre:str, costo_delivery: int): #este es el constructor de la tienda. Los argumentos "vienen de la calle"
        self.__nombre = nombre  #esto viene de afuera (por argumento)
        self.__costo_delivery = costo_delivery #esto viene de afuera (por argumento)
        self.__productos = []  #esta variable es de uso interno de la tienda (no viene de afuera)

    @abstractmethod
    def ingresar_producto(self, nombre: str, precio:int, stock:int):
        pass

    @abstractmethod
    def listar_producto(self):
        pass

    @abstractmethod
    def realizar_venta(self, nombre :str, cantidad: int):
        pass

    @property
    def nombre(self):
        return self.__nombre

    @property
    def costo_delivery(self):
        return self.__costo_delivery
    
    @property
    def productos(self):
        return self.__productos



class TiendaRestaurante(Tienda):
    tipo = "Restaurante"
  
    def ingresar_producto(self, nombre: str, precio: int, stock: int = 0) -> None:   #decia def ingresar_producto(self, nombre: str, precio: int, stock: int):

        p = Producto(nombre, precio, 0) #elimine str e int. estaba como (nombre: str, precio: int, stock: int)

        if p in self.productos:
            pass
        
        else:
            self.productos.append(p)



    def listar_producto(self):
        lista = []
        for producto in self.productos:
            lista.append((producto.nombre, producto.precio))
        return lista   
    
    def realizar_venta(self, nombre: str, cantidad: int):
        pass

class TiendaSupermercado(Tienda):
    tipo = "Supermercado"

    def ingresar_producto(self, nombre: str, precio: int, stock: int) -> None: 

        p = Producto(nombre, precio, stock) 

        if p in self.productos:
            indice = self.productos.index(p)
            self.productos[indice] += p
        
        else:
            self.productos.append(p)

    def listar_producto(self):
        lista = []
        for producto in self.productos:
            mensaje = "Pocos productos disponibles"
            if producto.stock < 10:
                lista.append((producto.nombre, producto.precio, producto.stock, mensaje))
            else:
                lista.append((producto.nombre, producto.precio, producto.stock))      
        return lista  

    def realizar_venta(self, nombre: str, cantidad: int):
        
        venta = Producto(nombre, 5000, cantidad ) 

        if venta in self.productos:
            indice = self.productos.index(venta)
            if cantidad > self.productos[indice].stock:
                self.productos[indice].stock = 0
        
            else: 
                self.productos[indice] -= venta
        else:
            pass 


class TiendaFarmacia(Tienda):
    tipo = "Farmacia"

    def ingresar_producto(self, nombre: str, precio: int, stock: int) -> None: 

        p = Producto(nombre, precio, stock) 

        if p in self.productos:
            indice = self.productos.index(p)
            self.productos[indice] += p
        
        else:
            self.productos.append(p)

#no se puede solicitar una cantidad superior a 3 por producto en cada venta
#“Envío gratis al solicitar este producto” junto al precio de los productos con un valor superior a $15.000.
    def listar_producto(self):
        lista = []
        for producto in self.productos:
            mensaje = "Envío gratis al solicitar este producto"
            if producto.precio > 15000:
                lista.append((producto.nombre, producto.precio, producto.stock, mensaje))
            else:
                lista.append((producto.nombre, producto.precio, producto.stock))     
        return lista  


    def realizar_venta(self, nombre: str, cantidad: int):
        if cantidad <= 3:
            venta = Producto(nombre, 5000, cantidad ) 

            if venta in self.productos:
                indice = self.productos.index(venta)
                if cantidad > self.productos[indice].stock:
                    self.productos[indice].stock = 0
                else: 
                    self.productos[indice] -= venta
                
            else:
                pass 
        else:
            pass
        

if __name__ == "__main__":

    f01 = TiendaFarmacia('DrSami', 1000)
    super01 = TiendaSupermercado('Santa Isabela', 2000)
    restobar01 = TiendaRestaurante('Los Pollos Hermanos', 1500)

    print(super01.listar_producto())

    super01.ingresar_producto('Pavo 200 gr', 1500, 20)
    print(super01.listar_producto())
    super01.ingresar_producto('pavo 200 gr', 1500, 30)
    print(super01.listar_producto())

    super01.ingresar_producto('Leche 1lt', 900, 30)
    print(super01.listar_producto())

    print("***resumen de productos en super01:***")
    for item in super01.listar_producto():
        print(item)
    print("----------------------")

    f01.ingresar_producto('Aspirina', 1500, 20)
    print(f01.listar_producto())
    f01.ingresar_producto('Aspirina', 1500, 30)
    print(f01.listar_producto())

    f01.ingresar_producto('Nexium', 2000, 100)
    print(f01.listar_producto())

    f01.realizar_venta('Aspirina', 5)
    print(f01.listar_producto(), "no realiza la venta porque el máximo permitido es 3")
    

    f01.realizar_venta('Nexium', 2)
    print(f01.listar_producto())
    print(f"Venta exitosa. Gracias por comprar en {f01.nombre}")

####################################################################################
