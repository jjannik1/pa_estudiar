merged = {}

def run(d1: dict, d2: dict) -> dict:
    # TODO
    global merged

    for i,j in d1.items():
        merged[i] = j

    for l,n in d2.items():
        merged[l] = n






    return merged


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(merged)
