compras = {
   "Juan Pérez": [
       {"producto": "Teclado", "cantidad": 1, "precio_unitario": 25.99},
       {"producto": "Ratón", "cantidad": 2, "precio_unitario": 15.50}
   ],
   "Ana Gómez": [
       {"producto": "Monitor", "cantidad": 1, "precio_unitario": 150.00}
   ]
}


while True:
    print()
    print("Menu")
    print("1. Mostrar compras de un cliente")
    print("2. Añadir una nueva compra para un cliente")
    print("3. Calcular el total gastado por un cliente")
    print("4. Mostrar el cliente con mayor gasto total")
    print("5. Salir")
    print()

    opc = int(input("Elige una opcion: "))

    if opc == 1:
        clin = input("Quien eres: ")
        if clin in compras:
            print(f'Compras de {clin}')
            lista_pedidos = compras[clin]
            

            for i in lista_pedidos:
                print(f'- ',end=" ")
                for x , j in i.items():
                    print(f'{x}: {j}', end=", ")
                print()
                
        else:
            print("Cliente no existente")


    elif opc == 2:
        nombre_cliente = input("Introduce el nombre del cliente: ")

        if nombre_cliente not in compras:
            compras[nombre_cliente]=[]
            producto_nuevo = ()

            nombre_producto = input("introduce el nombre del producto: ")
            cantidad_producto = input("Introduce la cantidad del producto: ")
            precio_producto = input("Introduce el precio del producto: ")

            producto_nuevo = {"producto": nombre_producto, "cantidad": cantidad_producto, "precio_unitario":precio_producto}
            compras[nombre_cliente].append(producto_nuevo)
        else:
            producto_nuevo = ()

            nombre_producto = input("introduce el nombre del producto: ")
            cantidad_producto = input("Introduce la cantidad del producto: ")
            precio_producto = input("Introduce el precio del producto: ")

            producto_nuevo = {"producto": nombre_producto, "cantidad": cantidad_producto, "precio_unitario":precio_producto}
            compras[nombre_cliente].append(producto_nuevo) 

    elif opc == 3:
        total_gastado = 0
        nombre_cliente = input("Introduce el nombre del cliente: ")
        if nombre_cliente in compras:
          lista_pedidos = compras[nombre_cliente]

          for pedido in lista_pedidos:
              total_gastado += pedido["cantidad"]*pedido["precio_unitario"]

          print(f'El total gastado es {total_gastado} de {nombre_cliente}')
        else:
            print("Cliente no tiene pedidos")

    elif opc== 3:
        pass