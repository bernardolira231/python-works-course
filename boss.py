import random
print("Escapa de tu escuela\n"
      "--------------------\n"
      "Tu estas detenido en la direccion de tu escuela y te tienes que quedar ahi hasta\n"
      "las 8 pm, pero ese dia es la fiesta mas grande de la historia ademas habias invitado a la chica que\n"
      "te gusta para ir juntos.\n"
      "A las 5 pm la directora se levanta de su silla y se va al salon de profesores es tu oportunidad de\n"
      "escapar abres la puerta y tienes dos caminos, Que camino tomas?\n"
      "\n")

opcion = input("[OPCION (A) - El lado izquierdo] | [OPCION (B) - El lado derecho] | [OPCION (C) - Esperas\n"
               "a que la directora regrese y tomas el castigo completo aunque no asistas a la fista]\n")

if opcion == "A":
    boligrafo = False
    print("Empiezas a caminar hacia el pasillo izquierdo y encuentras un boligrafo, lo tomas?\n"
          "\n")

    opcion = input(("[OPCION (A) - Tomas el boligrafo] | [OPCION (B) - Lo dejas en el piso]\n"))
    if opcion == "A":
        print("Tomas el boligrafo y lo guarda en tu mochila, tal vez te sirva\n")
        boligrafo = True
    elif opcion == "B":
        print("Dejas el boligrafo ya que no crees que te sirva de nada\n")
        boligrafo = False

    print("Caminas hacia el pasillo de la izquierda en la mitad del pasillo hay una puerta del salon 105\n"
          "dentro del salon hay un profesor el cual esta viendo hacia la puerta, Que haces?\n")
    opcion = input("[OPCION (A) - Avientas el boligrafo a una ventana] | [OPCION (B) - Caminas con normalidad]\n"
                   "[OPCION (C) - Regresas a la direccion]\n")
    if opcion ==  "A" and boligrafo == True:
        boligrafo = False
        print("Tiras el boligrafo hacia una ventana, el profesor se distrae y voltea hacia la ventana logras pasar,\n"
              "caminas recto y giras a la derecha encuentras al bravcucon de la escuela y te dice que si no\n"
              "le das un boligrafo te va a acusar con la directora")
        opcion = input("[OPCION (A) - Le das el boligrafo] | [OPCION (B) - Sales corriendo]\n")
        if opcion == "A":
            print("Tiraste la boligrafo para distraer al profesor por lo cual te quedaste sin boligrafo, el\n"
                  "bravcucon le grita a la directora y te regresa a la direccion ademas te castiga otros 3\n"
                  "dias por intentar escapar")
            exit()
        elif opcion == "B":
            print("Al salir corriendo el bravcucon le grita a la directora y ella te regresa a la direccion\n"
                  "ademas te castiga otros 3 dias por intentar escapar")
            exit()
    elif opcion == "A" and boligrafo == False:
        print("No agarraste el boligrafo, la directora te ve al lado de la puerta y te regresa a la direccion\n"
              "ademas te castiga otros 3 dias por intentar escapar")
        exit()
    elif opcion == "B":
        print("Caminas tranquilo hacia el otro lado y el profesor no se inmuta, caminas recto y giras a la\n"
              "derecha encuentras al bravcucon de la escuela y te dice que si no le das un boligrafo te va\n"
              "a acusar con la directora\n")
        opcion = input("[OPCION (A) - Le das el boligrafo] | [OPCION (B) - Sales corriendo]\n")
        if opcion == "A":
            contrasena_random = random.randint(1, 25)
            print("Por suerte agarraste el boligrafo y todavia lo tienes en tu mochila, lo sacas y se lo das,\n"
                  "el bravcucon te deja seguir avanzando y llegas a la puerta de salida, la puerta tiene un\n"
                  "candado y arriba de este viene escrito lo siguiente,\n"
                  "La respuesta de esta operacion es la llave de este candado:\n"
                  "La operacion es: 3 * {}".format(contrasena_random))
            opcion = int(input("Cual es el resultado?\n"))
            if opcion == (3 * contrasena_random):
                print("Genial se abrio la puerta, la abres y sales.")
                print("ERES LIBRE, Vas con la chica y juntos disfrutan la fiesta")
                exit()
            else:
                print("La respuesta es incorrecta, suena una alarma y la directora llega y te regresa a la\n"
                      "direccion ademas te castiga otros 3 dias por intentar escapar.")
                exit()
    elif opcion == "C":
        print("Regresas triste y derrotado a la direccion, la directora regresa y te ve sentado en la direccion\n"
              "te pregunta porque y le cuentas de la fiesta, te dice que por hoy te dejara salir para que\n"
              "no te pierdas la cita.")
        exit()
elif opcion == "B":
    print("Caminas recto y ves la puerta de salida corres para llegar pero ves que a mitad del pasillo esta\n"
          "la puerta del salon en el que esta la directora y si avanzas te vera, Que haces?")
    opcion = input("[OPCION (A) - Regresas a la direccion] | [OPCION (B) - Caminas lento para no hacer ruido]\n")
    if opcion == "A":
        print("Regresas triste y derrotado a la direccion, la directora regresa y te ve sentado en la direccion\n"
              "te pregunta porque y le cuentas de la fiesta, te dice que por hoy te dejara salir para que\n"
              "no te pierdas la cita.")
        print("ERES LIBRE, Vas con la chica y juntos disfrutan la fiesta")
        exit()
    elif opcion == "B":
        print("Caminas lento para no hacer ruido pero justo en ese momento la directora sale del salon,\n"
              "Que haces?\n")
        opcion = input("[OPCION (A) - Le dices que ibas al sanitario] | [OPCION (B) - Le dices que ibas a\n"
                       "buscarla]\n")
        if opcion == "A":
            print("Le dices que ibas al sanitario pero la directora te dice que de ese lado no hay ningun\n"
                  "sanitario y se da cuenta que quieres escapar, te lleva a la direccion y ademas te castiga\n"
                  "otros 3 dias por intentar escapar.")
            exit()
        elif opcion == "B":
            print("Le dices que ibas a buscarla para decile algo\n"
                  "le cuentas de la fiesta, te dice que por hoy te dejara salir para que no te pierdas la\n"
                  "cita.")
            print("ERES LIBRE, Vas con la chica y juntos disfrutan la fiesta")
            exit()
elif opcion == "C":
    print("Regresas triste y derrotado a la direccion, la directora regresa y te ve sentado en la direccion\n"
              "te pregunta porque y le cuentas de la fiesta, te dice que por hoy te dejara salir para que\n"
              "no te pierdas la cita.")
    print("ERES LIBRE, Vas con la chica y juntos disfrutan la fiesta")
    exit()
