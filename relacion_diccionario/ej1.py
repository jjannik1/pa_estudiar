usuarios = {
   "juanperez": {"correo": "juan@example.com", "contraseña": "1234", "rol": "admin"},
   "anagomez": {"correo": "ana@example.com", "contraseña": "abcd", "rol": "editor"}
}


while True:
    print("Menu")
    print("1. Ver todos los usuarios")
    print("2. Añadir un nuevo usuario")
    print("3. Cambiar el rol de un usuario")
    print("4. Salir")

    print()
    opc = int(input("Selecciona una opción: "))
    print()

    if opc == 1:
        for i in usuarios:
            dicc = usuarios[i]
            print(i, ":", "Correo",":", dicc["correo"], ",", "Rol",":", dicc["rol"])

    elif opc == 2:


        new_user = input("Introduce nuevo usuario: ")
        if new_user not in usuarios:
        
            usuarios[new_user] = {}
            dicci = {}
            coreo = input("Introduce su correo: ")
            contrase = input("Introduce su contraseña: ")
            rolo = input("Introduce su rol: ")

            dicci["correo"] = coreo
            dicci["contraseña"] = contrase
            dicci["rol"] = rolo

            usuarios[new_user] = dicci
        else:
            print("Ese usuario ya existe")
            print()


    elif opc == 3:
        x = input("Que usuarios quieres cambiar de rol: ")
        if x in usuarios:
            dicc = usuarios[x]
            rol = input("Introduce el nuevo rol: ")
            dicc["rol"] = rol
            usuarios[x] = dicc

        else:
            print("Usuario no existe")


    elif opc == 4:
        break



        