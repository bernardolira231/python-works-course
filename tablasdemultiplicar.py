numero_del_usuario = int(input('Que tabla de multiplicar quieres saber:\n'))

for n in range(1,11):
    if (n % 2) == 0:
        print('{} * {} = {}'.format(numero_del_usuario, n, numero_del_usuario * n))
