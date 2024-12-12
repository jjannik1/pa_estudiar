pedidos = {
   "PED001": {"cliente": {"nombre": "Juan Pérez", "correo": "juan@example.com"}, "productos": ["Teclado", "Ratón"]},
   "PED002": {"cliente": {"nombre": "Ana Gómez", "correo": "ana@example.com"}, "productos": ["Monitor"]}
}


while True:
    print("Menu")
    print("1. Ver pedidos por cliente")
    print("2. Añadir un nuevo pedido")
    print("3. Eleminar un pedido")
    print("4. Salir")

    print()
    opc = int(input("Selecciona una opción: "))
    print()

    if opc == 1:
        encontrado = True
        print()
        clin = input("Introduce el nombre del cliente para ver sus pedido: ")
        for i, j in pedidos.items():
            if clin in j["cliente"]["nombre"]:
                print(i)
                
            encontrado = False
                

        print(f'Pedidos de {clin}:')
        for x in pedidos[i]["productos"]:
                print(f'- {x}')
        print()
    elif opc == 2:
        new_code = input("Introduce su clave de pedido: ")
        if new_code not in pedidos:
             pedidos[new_code] = {}
             productos = []

             nombre_cliente = input("Introduce su nombre: ")
             correo_cliente = input("Introduce su correo: ")

             while True:
                  nombre_prod = input("Introduce nombre del producto o Salir para salirse: ")
                  if nombre_prod != "Salir":
                       productos.append(nombre_prod)
                  else:
                       break
             pedidos[new_code]=["cliente"]["nombre"] = nombre_cliente
             pedidos[new_code]["cliente"]["correo"] = correo_cliente
             pedidos[new_code]["cliente"]["productos"] = productos[:]

        else:
             print("Ya existe la clave de un pedido")



    elif opc == 3:
         clave_pedido = input("Introduce clave pedido")

         if clave_pedido in pedidos:
              pedido_eliminiado = pedidos.pop(clave_pedido)

              print("Se ha eliminado el pedido")
         else:
            print("Pedido no existe")