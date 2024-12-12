pedidos = {
   "PED001": {
       "cliente": {"nombre": "Juan Pérez", "correo": "juan@example.com"},
       "productos": [
           {"producto": "Teclado", "cantidad": 1, "precio_unitario": 25.99},
           {"producto": "Ratón", "cantidad": 2, "precio_unitario": 15.50}
       ],
       "estado": "pendiente"
   },
   "PED002": {
       "cliente": {"nombre": "Ana Gómez", "correo": "ana@example.com"},
       "productos": [
           {"producto": "Monitor", "cantidad": 1, "precio_unitario": 150.00}
       ],
       "estado": "enviado"
   }
}


while True:
    print()
    print("Menu")
    print("1. Ver pedidos y su estado")
    print("2. Cambiar el estado de un pedido")
    print("3. Calcular la factura de un pedido")
    print("4. Añadir un nuevo pedido")
    print("5. Salir")
    print()

    opc = int(input("Selecciona una opcion: "))
    print()

    if opc == 1:
        for i,j in pedidos.items():
            print(f'El Pedido: {i}')
            print(f'\t- Cliente: {j["cliente"]["nombre"]}')
            print(f'\t- Estado: {j["estado"]}')
            print()
        input()


    
    elif opc == 2:
        ped = input("Introduce la clave del pedido que quieres cambiar el estado: ")

        if ped in pedidos:
            dicc = pedidos[ped]
            est = input("A que estado quieres ponerle(pendiente,enviado,entregado): ")
            dicc["estado"] = est
            pedidos[ped] = dicc
            
        else: 
            print("Pedido no existe")



    elif opc == 3:
        ped = input("Introduce la clave del pedido que quieres calcular la factura: ")
        if ped in pedidos:
            dicc = pedidos[ped]
            total = 0
            for producto in dicc["productos"]:
                total += producto["cantidad"] * producto["precio_unitario"]

            print(f'El precio total del pedido {ped} es {total:.2f}')

        else:
            print("Producto no existe")


    elif opc == 4:
        cod = input("Introduce su codigo de pedido(PED###): ")
        if cod in pedidos:
            print("Ese codigo de pedido ya existe.")
        else:
            cli = input("Introduce su nombre: ")
            corr = input("Introduce su correo: ")


            prod = input("Introduce el producto que quieres comprar: ")
            cant = int(input("introduce la cantidad que quieres de ese producto: "))
            precio = float(input("Introduce el precio del producto"))

            pedidos[cod] = {"cliente": {"nombre": cli, "correo": corr},"productos":[ {"producto": prod, "cantidad":cant, "precio_unitario":precio },],"estado":"pendiente"}

        



    elif opc == 5:
        break