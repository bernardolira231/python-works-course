respuesta = None

while respuesta != "A" and respuesta != "B" and respuesta != "C":
    respuesta = input("Que opcion prefieres [A, B, C]?")

if respuesta == "A":
    print("Has elegido bien")
elif respuesta == "B":
    print("Pudiste elegir mejor")
elif respuesta == "C":
    print("Elegiste mal")
