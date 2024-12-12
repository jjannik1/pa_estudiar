all_same = ""
verdad = True
def run(items: dict) -> bool:
    # TODO
    global all_same

    for i in items.values():
        for j in items.values():
            if i != j:
                verdad = False
                break
            




    return all_same


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(f'El diccionario es {verdad}')
