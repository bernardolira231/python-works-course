def pregunta():
    decicion = input('Estas seguro: ')
    if decicion == 'Si':
        print(True)
        return decicion
    elif decicion == 'No':
        print(False)
        return decicion
    return decicion


def main():
    pregunta()


if __name__ == '__main__':
    main()
