# En este programa se ingresa un valor en metros y se convertira en kilometros BLRA
valormetros = 0
valorkm = 0

valormetros = int(input("Ingresa un valor en metros para convertirlo en kilometros\n"))
valorkm = int((valormetros * 1)/1000)
print('La conversion de {} metros a kilometros es de: {} km'.format(valormetros, valorkm))
