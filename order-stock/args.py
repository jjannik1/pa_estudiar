stock = {'pen': 20, 'cup': 11, 'keyring': 40}


while True:
    merch = input("Introduce que producto quieres: ")

    if merch in stock.keys():
        break
    else:
        print("Tiene que estar en nuestro stock")

amount = int(input("Introduce la cantidad del stock: "))

print(stock(merch) > amount)