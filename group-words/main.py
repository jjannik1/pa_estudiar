group_words = {}

def run(words: list) -> dict:
    # TODO
    global group_words

    for palabra in words:
        primera_letra = palabra[0]

        if primera_letra not in group_words:
            group_words[primera_letra] = []

        group_words[primera_letra].append(palabra)

    print(group_words)









    return group_words


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
