def es_impar(numero):

    if numero % 2 == 0:
        impar = False
        print(impar)
        return impar

    else:
        impar = True
        print(impar)
        return impar


def main():

    es_impar(3)

    es_impar(24)


if __name__ == "__main__":
    main()
