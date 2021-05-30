def potencia(numero, base = 2):
    resultado = numero
    for a in range(1, base):
        resultado *= numero
    return resultado


def main():
    print(potencia(2))

    print(potencia(2, 3))

    print(potencia(2, 4))

    print(potencia(3, 9))


if __name__ == "__main__":
    main()
