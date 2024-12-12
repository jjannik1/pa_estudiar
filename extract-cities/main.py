cities = {}


def run(cinfo: str) -> dict:
    # TODO

    b = cinfo.split(";")

    for i in b:
        lista_clave_valor = i.split(":")
        print(lista_clave_valor)
        print()
        cities[lista_clave_valor[0]] = int(lista_clave_valor[1])
    print(cities)


    
    return cities


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
