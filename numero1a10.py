import random
valordelusr = int(input("Ingresa un numero del 1 al 10: "))
valorganador = random.randint(1,10)

if valordelusr != valorganador :
    print("Has perdido tu numero y el numero ganador son dieferentes")
    print("El numero ganador era {}".format(valorganador))
if valordelusr == valorganador :
    print("Has ganado el numero ganador es {}".format(valorganador))

