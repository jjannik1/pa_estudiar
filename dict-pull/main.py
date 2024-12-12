pdata = {}



def run(data: dict, target_keys: tuple) -> dict:
    # TODO
    global pdata

    for i in target_keys:
        valor = data[i]
        pdata[i] = valor






    return pdata


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(pdata)