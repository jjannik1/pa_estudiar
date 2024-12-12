numbers = [2, 3, 5, 3, 2, 1, 8, 2]
dic = {}
nrep = int(input("Introduce cuantos veces se repite: "))

for i in numbers:
    dic[i] = 0

for i in numbers:
    dic[i] += 1

for i in numbers:
    for j,v in dic.items():
        if v == nrep:
            print(f'El primer numero que se repite {nrep} veces es {j}')
            exit()
