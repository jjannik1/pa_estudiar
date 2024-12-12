avg_data = {}


def run(pdata: dict) -> dict:
    # TODO
    global avg_data

    valor_total = 0
    lista_resultado = []

    valor = pdata.values()
    claves = pdata.keys()

    for i in valor:
        valor_total = valor_total + i
    """
    for e in valor:
        resultado = e / valor_total * 100
        resultado = round(resultado,3)
        lista_resultado.append(resultado)
    
    for e , j in zip(claves, lista_resultado):
        avg_data[e] = j
    """

    #Esto es la version cortada de lo de arriba menos el round
    for e , j in pdata.items():
        avg_data[e] = j / valor_total * 100








    return avg_data


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(avg_data)
