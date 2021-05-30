def mayus(frase):
    caracteres = []
    for a in frase:
        if a.islower() == True:
            mayuss = a.swapcase()
            caracteres.append(mayuss)

        else:
            notcha = a
            caracteres.append(notcha)

    final = "".join(caracteres)
    print(final)
    return final


def main():
    mayus('Hola Como Estas')


if __name__ == "__main__":
    main()
