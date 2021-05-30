print("Bienvenido a mi conversor de Fahrenheit a Celcius")

temperaturaf = int(input("Dame tu temperatura en grados Fahrenheit: " ))
temperaturac = int((temperaturaf - 32)*5 / 9)

print("La temperatura en Celcius seria: {} grados celcius".format(temperaturac))
