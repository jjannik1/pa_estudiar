carrito = {
"Teclado": {"cantidad": 2, "precio_unitario": 25.99},
"Ratón": {"cantidad": 1, "precio_unitario": 15.50}
}

while True:
    print()
    print("Menu")
    print("1. Ver total del carrito")
    print("2. Añadir un producto")
    print("3. Modificar la cantidad de un producto")
    print("4. Salir")

    print()
    opc = int(input("Selecciona una opción: "))
    print()

    if opc == 1:
        total = 0
        for i in carrito:
            total += carrito[i]["cantidad"] * carrito[i]["precio_unitario"]
        print(f'Total del carrito: {total:.2f}€')

    elif opc == 2:
        prod = input("Introduce el producto que quieres comprar: ")
        cant = int(input("Introduce la cantidad del producto: "))
        prec = float(input("Introduce su precio: "))

        carrito[prod] = {"cantidad": cant, "precio_unitario": prec}

    elif opc == 3:
        prod = input("¿Que producto quieres modificar?: ")
        if prod in carrito:
            cant = int(input("Introduce la cantidad que quieres comprar del producto: "))
            carrito[prod]["cantidad"] = cant

    elif opc == 4:
        break