def suma(numbers):
    resultado = 0
    for number in numbers:
        resultado += number
    print(resultado)
    return resultado


def main():
    suma([1, 2, 3, 4, 5])


if __name__ == "__main__":
    main()
