
inventario = [ ["Teclado", 25.99, 10], ["Ratón", 15.50, 20], ["Monitor", 150.00, 5] ]


while True:
    print("Menú:")
    print("1. Ver productos")
    print("2. Añadir producto")
    print("3. Modificar producto")
    print("4. Salir")



    n = int(input("Selecciona una opción: "))

    if n == 1:
        print("Productos:")
        for i in inventario:
            print(f'- {i[0]} : Precio: {i[1]}, Stock: {i[2]}')

    elif n == 2:
        prod = str(input("Introduce producto: "))
        existe = False
        for i in inventario:
           if(prod == str(f'{i[0]}')):
               existe = True
               break
        if existe == True:
               print("Producto ya esta en la lista")
               continue
        
        
        cost = float(input("Introduce precio del producto: "))
        lage = int(input("Introduce cuantos veces tenemos de stock "))

        vacio = []
        vacio.append(prod)
        vacio.append(cost)
        vacio.append(lage)

        inventario.append(vacio)

    elif n == 3:
        print("1. Modificar Precio")

        print("2. Modificar Stock")

        print("3. Menu Principal")

        h = int(input("Elige opcion"))
        if h == 3:
            break
    
    elif h == 2:

        k = str(input("Introduce producto que quieres cambiar stock: "))
        if k not in inventario:
               print("Producto no esta en el inventario")
               continue
               
        j = int(input("Introduce el stock del producto {k}: "))
        for k in inventario:
               inventario[0][2] == j

        
            
    elif n == 4:
        break
    else:
        print("Debes coger uno de las opciones")
        continue

