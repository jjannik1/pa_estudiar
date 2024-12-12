productos = {
   "Electrónica": ["Teclado", "Ratón", "Monitor"],
   "Hogar": ["Mesa", "Silla", "Lámpara"]
}

while True:
    print("Menu")
    print("1. Ver productos de una categoría")
    print("2. Añadir un producto a una categoría")
    print("3. Crear una nueva categoría")
    print("4. Salir")

    print()
    opc = int(input("Selecciona una opción: "))
    print()

    if opc == 1:
        cat = input("Que categoria quieres ver: ")
        if cat in productos:
            print(f'Productos en {cat}: ')
            for i in productos[cat]:
                print(i)
                
        else:
            print("Categoria no existe")

    elif opc == 2:
        cat = input("A que categoria quieres añadir el producto")
        if cat in productos:
            lista = productos[cat]
            producto = input("Que producto quieres meter")

            if producto not in lista:
                lista.append(producto)
                productos[cat] =lista

            else:
                print("Producto ya existe")
        else:
            print("Cayegoria no existe")

    
    elif opc == 3:
        cat = input("Introduce nombre de la nueva categoria: ")
        if cat not in productos:
            productos[cat] = []
        else: 
            print("Categoria ya existe")

    elif opc == 4:
        break