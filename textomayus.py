import string
texto_usuario = input('Ingresa un texto:\n')
letras_mayus = 0

for letra in texto_usuario:
    if letra in string.ascii_uppercase:
        letras_mayus += 1
print('Hay {} letras mayusculas en total'.format(letras_mayus))
