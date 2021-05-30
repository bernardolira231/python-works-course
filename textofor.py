texto_usuario = input('Pon un texto para ver cuantos espacios, puntos y comas tiene\n')
espacios = 0
puntos = 0
comas = 0

for letra in texto_usuario:
    if letra == " ":
        espacios += 1
    elif letra == ".":
        puntos += 1
    elif letra == ",":
        comas += 1

print('Espacios: {}, Puntos: {}, Comas: {}'.format(espacios, puntos, comas))
