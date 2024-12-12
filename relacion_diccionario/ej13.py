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

    if opc == 1:
        for i,j in pedidos.items():
            print(f'{i}: {j}')


    
    elif opc == 2:
        ped = input("Introduce la clave del pedido que quieres cambiar el estado: ")
        if ped in pedidos:
            est = input("A que estado quieres ponerle(pendiente,enviado,entregado): ")
            
