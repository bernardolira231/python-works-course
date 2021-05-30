edad = int(input("Dime tu edad: "))
tipo_de_credencial = \
    input("Que tipo de credencial tienes (E para Estudiante / P para pensionado / F para familia numerosa / N nada: ")

if (25<= edad <= 35 and tipo_de_credencial =="E") or \
        edad <= 10 or (edad >= 65 and tipo_de_credencial == "P") or \
        (tipo_de_credencial == "F"):
    print("Se te aplica el descuento")

else :
    print("No se aplica el descuento")

