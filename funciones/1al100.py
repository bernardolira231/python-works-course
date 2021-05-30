import random


def adivina(num):
    numadivinar = random.randint(1, 100)
    if numadivinar == num:
        print("Has adivinado el numero")
    else:
        print("El numero era {} vuelve a intentarlo".format(numadivinar))
    return


def main():
    adivina(num = int(input('Escoge un numero entre 1 y 100 y si escoges el numero correcto ganaras: ')))


if __name__ == '__main__':
    main()
