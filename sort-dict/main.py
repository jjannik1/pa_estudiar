sorted_items = []

def run(unsorted_items: dict) -> list[tuple]:
    # TODO
    global sorted_items

    lista = []

    claves = list(unsorted_items.keys())
    valores = list(unsorted_items.values())
    valor_ord = sorted(valores)


    for i in valor_ord:
        posicion = valores.index(i)
        clave = claves[posicion]
        tupla = (clave,i)
        lista.append(tupla)

    print(lista)



    return sorted_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
