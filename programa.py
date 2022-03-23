from tienda import TiendaRestaurante, TiendaFarmacia, TiendaSupermercado

opcion_ingreso = int(input("Elige tienda: 1.Restaurante 2.Farmacia 3.Supermercado 4.Salir \n > "))

if opcion_ingreso == 4:
    print("Hasta pronto")
    exit()
elif opcion_ingreso == 1:
    nombre = input("\nIngrese nombre de la tienda: \n")
    costo_delivery = int(input("\nIngrese costo delivery: \n"))
    tienda01=TiendaRestaurante(nombre, costo_delivery)

elif opcion_ingreso == 2:
    nombre = input("\nIngrese nombre de la tienda: \n")
    costo_delivery = int(input("\nIngrese costo delivery: \n"))
    tienda01=TiendaFarmacia(nombre, costo_delivery)

elif opcion_ingreso == 3:
    nombre = input("\nIngrese nombre de la tienda: \n")
    costo_delivery = int(input("\nIngrese costo delivery: \n"))
    tienda01=TiendaSupermercado(nombre, costo_delivery)

#ingresar productos
pregunta_seguir= int(input("Quiere ingresar un producto? 1. Si 2. No \n > "))

while pregunta_seguir == 1:
    nombre = input("\nIngrese nombre del producto: \n")
    precio = int(input("\nIngrese precio del producto: \n"))
    stock = int(input("\nIngrese stock del producto:\n"))
    tienda01.ingresar_producto(nombre, precio, stock)
    
    pregunta_seguir = int(input("quiere ingresar otro producto? 1. Si 2. No \n > "))
    if pregunta_seguir == 2:
        print("Ha finalizado el ingreso de productos")
        break


#### Operaciones a realizar

flag = 0
while flag == 0:

    pregunta_operacion = int(input("__Menú__ \n ¿Qué operación desea realizar? 1. Listar Productos 2. Realizar Venta 3. Salir \n > "))

    #listar productos
    if pregunta_operacion == 1:
        lista_prod= tienda01.listar_producto()
        print(f"\n***** DATOS DEL INGRESO *****\n {tienda01.tipo} {tienda01.nombre}\n Lista de productos:\n {lista_prod}")
        pregunta_volver = int(input("¿Desea volver al Menú? 1. Si 2. No (Salir) \n > "))
        if pregunta_volver == 1:
            flag = 0
        else:
            print("Hasta pronto")
            exit()

    #venta
    elif pregunta_operacion == 2:
        while pregunta_operacion == 2:
            nombre = input("\nIngrese nombre del producto: \n")
            cantidad = int(input("\nIngrese la cantidad a vender: \n"))
            tienda01.realizar_venta(nombre, cantidad)
        
            pregunta_operacion = int(input("quiere finalizar la venta? 1. Si 2. No \n > "))
            if pregunta_seguir == 1:
                print("Ha finalizado la operación")
                break
    #salida
    else:
            print("Hasta pronto")
            exit()
