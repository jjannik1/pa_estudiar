fixed_db = []


def run(db: list) -> list:
    # TODO
    global fixed_db
    cont = 0


    for i in db:
        cont += 1
        i['id'] = cont
        fixed_db.append(i)







    return fixed_db


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    for i in fixed_db:
        print(i)