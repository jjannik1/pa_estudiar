
n200 = 0
n100 = 0
n50 = 0
euro1 = "Moneda de 1 euro"
euro2 = "Moneda de 2 euro"
ce50 = "Moneda de 50 centimos"
vuelta = {}
verdad = True

cambio = float(input("Introduce vuelta en €: "))


if cambio == 0:
    vuelta = {}
    print(f"Tu vuelta es {vuelta}")


cambio = cambio *100

while verdad:

    while cambio >= 200:
        n200 += 1
        cambio -= 200


    while cambio >= 100:
        n100 += 1
        cambio -= 100

    while cambio >= 50:
        n50 += 1
        cambio -= 50
    vuelta[euro2] = n200
    vuelta[euro1] = n100
    vuelta[ce50] = n50

    print(f'Su vuelta es {vuelta}')

    verdad = False

