pedidos = [
["Juan Pérez", "Teclado", "pendiente"], 
["Ana Gómez", "Monitor", "enviado"], 
["Luis Torres", "Ratón", "entregado"] 
]



while True:
    print("Menú:")
    print("1. Ver productos")
    print("2. Añadir producto")
    print("3. Modificar producto")
    print("4. Salir")



    n = int(input("Selecciona una opción: "))

    if n == 1:
        print("Productos:")
        for i in pedidos:
            print(f'- {i[0]}  {i[1]} {i[2]}')
