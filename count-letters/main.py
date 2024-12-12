counter = {}


def run(text: str) -> dict:
    # TODO
    global counter

    for i in text:
        contador = 1

        for j in text[text.index(i)+1:]:
            if i == j : 
                contador = contador + 1
        if i in counter : 
            pass
        else:
            counter[i] = contador



    


    return counter


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(counter)
