from random import randint
import os

vida_inicial_pikachu = 80
vida_inicial_squirtle = 90
TAMANO_BARRA = 20
vida_pikachu = vida_inicial_pikachu
vida_squirtle = vida_inicial_squirtle

while vida_pikachu > 0 and vida_squirtle > 0:
    # Se desenvuelve el combate

    if vida_pikachu <= 0:
        vida_pikachu = 0
    elif vida_squirtle <= 0:
        vida_squirtle = 0

    # Turno de Pikachu
    print("Turno de pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        # Bola voltio
        print("Pikachu ha lanzado Bola Voltio")
        vida_squirtle -= 10
    else:
        # Trueno
        print("Pikachu ha lanzado Trueno")
        vida_squirtle -= 11

    barra_de_vida_pikachu = int(vida_pikachu * TAMANO_BARRA / vida_inicial_pikachu)
    barra_de_vida_squirtle = int(vida_squirtle * TAMANO_BARRA / vida_inicial_squirtle)
    print("Pikachu:   [{}{}] ({}/{})".format("*" * barra_de_vida_pikachu, " "*(TAMANO_BARRA - barra_de_vida_pikachu),
                                             vida_pikachu, vida_inicial_pikachu))
    print("Squirtle:   [{}{}] ({}/{})".format("*" * barra_de_vida_squirtle, " " * (TAMANO_BARRA - barra_de_vida_squirtle),
                                              vida_squirtle, vida_inicial_squirtle))
    if vida_pikachu <= 0:
        vida_pikachu = 0
    elif vida_squirtle <= 0:
        vida_squirtle = 0

    input("Enter para continuar...\n\n")
    os.system ("clear")

    #Turno Squirtle
    print("Turno Squirtle")

    ataque_squirtle = None
    while ataque_squirtle not in ["P", "p", "A", "a", "B","b", "S", "s"]:
        ataque_squirtle = input("Que ataque deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja, [S]altas turno: ")

    if ataque_squirtle == "P" or "p":
        # Placaje
        print("Has usado Placaje")
        vida_pikachu -= 10

    elif ataque_squirtle == "A" or "a":
        # Pistola Agua
        print("Has usado Pistola Agua")
        vida_pikachu -= 12

    elif ataque_squirtle == "B" or "b":
        # Burbuja
        print("Has usado Burbuja")
        vida_pikachu -= 9

    elif ataque_squirtle == "S" or "s":
        #Saltas turno
        print("Saltas turno")

    if vida_squirtle <= 0:
        vida_squirtle = 0
    elif vida_pikachu <= 0:
        vida_pikachu = 0

    barra_de_vida_pikachu = int(vida_pikachu * TAMANO_BARRA / vida_inicial_pikachu)
    barra_de_vida_squirtle = int(vida_squirtle * TAMANO_BARRA / vida_inicial_squirtle)
    print("Pikachu:   [{}{}] ({}/{})".format("*" * barra_de_vida_pikachu, " "*(TAMANO_BARRA - barra_de_vida_pikachu),
                                             vida_pikachu, vida_inicial_pikachu))
    print("Squirtle:   [{}{}] ({}/{})".format("*" * barra_de_vida_squirtle, " " * (TAMANO_BARRA - barra_de_vida_squirtle),
                                              vida_squirtle, vida_inicial_squirtle))
    if vida_squirtle <= 0:
        vida_squirtle = 0
    elif vida_pikachu <= 0:
        vida_pikachu = 0

    input("Enter para continuar...\n\n")
    os.system ("clear")

if vida_pikachu == 0:
    print("Has ganado")
elif vida_squirtle == 0:
    print("Has perdido")
