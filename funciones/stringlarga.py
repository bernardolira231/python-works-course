def string_mas_larga(iterable, *args):
    if args:
        largo = [len(iterable)]
        for a in args:
            largo.append(len(a))
        if largo[0] > largo[1] and largo[0] > largo[2]:
            return iterable
        elif largo[1] > largo[0] and largo[1] > largo[2]:
            return args[0]
        elif largo[2] > largo[0] and largo[2] > largo[1]:
            return args[1]
        elif largo[0] == largo[1] and largo[0] > largo[2]:
            return iterable, args[0]
        elif largo[0] == largo[2] and largo[0] > largo[1]:
            return iterable, args[1]
        else:
            return args[0], args[1]
    return iterable


def main():
    print(string_mas_larga('hola', 'como', 'estas'))


if __name__ == "__main__":
    main()
