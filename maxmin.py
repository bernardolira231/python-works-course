numeros_introducidos = input('Introduzca los numeros separados  por coma: ')
numeros_de_usuario = numeros_introducidos.split(',')

numeros_de_usuario = [int(numero) for numero in numeros_de_usuario]

numero_pequeno = numeros_de_usuario[0]
numero_grande = numeros_de_usuario[0]

for numero in numeros_de_usuario[1:]:
    if numero_pequeno > numero:
        numero_pequeno = numero

    if numero_grande < numero:
        numero_grande = numero

print('Numero grande: {}, Numero pequeno {}'.format(numero_grande,numero_pequeno))
