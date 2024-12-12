servidores = {
"Servidor 1": {
"dominio": "example.com",
"peticiones": [1200, 1500, 1800, 2000],
"estado": "activo"
},
"Servidor 2": {
"dominio": "shop.com",
"peticiones": [800, 900, 1000, 1100],
"estado": "en mantenimiento"
}
}

while True:
    print()
    print("Menu")
    print("1. Mostrar configuración y estadísticas de todos los servidores.")
    print("2. Cambiar el estado de un servidor.")
    print("3. Mostrar servidor con más peticiones en un mes específico.")
    print("4. Añadir un nuevo servidor.")
    print("5. Salir")
    print()

    opc = int(input("Selecciona una opcion: "))

    if opc == 1:

        for i,j in servidores.items():
            print(f'El {i} tine {j}')

    elif opc == 2:

        serv = input("Introduce el servidor que quieres cambiar el estado: ")
        if serv in servidores:
            est = input("Introduce el estado (activo,inactivo,en mantenimiento): ")
            dicc = servidores[serv]
            dicc["estado"] = est
            servidores[serv] = dicc
        else:
            print("Servidor no existe")

 

    elif opc == 3:
        lista = {}
        dicc = []
        mes = int(input("Introduce el mes (1-4)"))
        if mes <= 4 and mes >=1:
            max_peticiones = 0
            servidor_max = ""
            for i, j in servidores.items():
                peticiones_mes = j["peticiones"][mes - 1]  # index 0 para enero, 1 para febrero, etc.
                if peticiones_mes > max_peticiones:
                    max_peticiones = peticiones_mes
                    servidor_max = i
            print(f"El servidor con más peticiones en el mes {mes} es {servidor_max} con {max_peticiones} peticiones.")
            
            
            
            #Aqui abajo son pruebas
            """            for i in servidores.items():
                    dicc = servidores[i]
                    lista += dicc["peticiones"](mes)
                print(lista)"""

        """for i in servidores.items():
            for x in servidores.items():
                dicc = x[i]"""
        
        """for i in servidores.values():
            print(i["peticiones"])"""
        
        #Nicht vergessen items von der position anfang +1 solange i sich widerholt und so weiter...
        
        """for i in servidores.items():
            print(i(+1)["peticiones"])"""

    elif opc == 4:
        serv = input("Introduce nombre del servidor: ")
        if serv not in servidores:
            dom = input("Intrdocue su dominio: ")
            peticiones = []
            for i in range(4):
                peticion = int(input("Introduce las peticiones del mes {i+1}"))
                peticiones.append(peticion)
            est = input("Introduce su estado: ")

            servidores[serv] = {"dominio" : dom, "peticiones": peticiones, "estado" :est}


            