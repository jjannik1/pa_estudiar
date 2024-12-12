unpack_items = {}


def run(items: list) -> dict:
    # TODO

    for i in items:
        unpack_items[i[0]] = i[1:]









    return unpack_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(unpack_items)
