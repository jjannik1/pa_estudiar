visitas = {
"example.com": [1000, 1200, 1100],
"shop.com": [2000, 2200, 2100]
}
while True:
    print()
    print("Menu")
    print("1. Ver promedio anual de visitas")
    print("2. Ver pagina con mas visitas en un mes")
    print("3. Añadir una nueva pagina")
    print("4. Salir")

    print()
    opc = int(input("Selecciona una opción: "))
    print()

    if opc == 1:
        for i , j in visitas.items():
            total = sum(j) / len(j)
            print(i)
            print(total)
    elif opc == 2:
        max_visitas = 0
        pagina_max_visitas = ""
        for pagina, visitas_lista in visitas.items():
            max_visita_mes = max(visitas_lista)
            if max_visita_mes > max_visitas:
                max_visitas = max_visita_mes
                pagina_max_visitas = pagina

    #elif opc == 3:
        """        pag = input("Introduce nombre de la pagina: ")
        if pag not in visitas:
            for i in len(visitas.values()):
                c = input("Introduce ")"""
    elif opc == 3:
        pag = input("Introduce nombre de la página: ")
    
        # Verificamos si la página ya existe en el diccionario
        if pag not in visitas:
            visitas_mes = []  # Lista donde se almacenarán las visitas para los meses

            # Pedimos las visitas para los 3 meses (puedes modificar la cantidad de meses si lo necesitas)
            for i in range(3):  # Asumiendo 3 meses de visitas
                c = int(input(f"Introduce las visitas para el mes {i+1}: "))
                visitas_mes.append(c)

            # Añadimos la nueva página con sus visitas
            visitas[pag] = visitas_mes
            print(f"Página {pag} añadida con éxito.")
        else:
            print("La página ya existe.")