peso_a_dolar = float(0.047)
dolar_a_peso = float(21.22)
dolar_a_euro = float(0.84)
euro_a_dolar = float(1.19)
peso_a_euro = float(0.040)
euro_a_peso = float(25.24)
dinero_final = 0
cambio_de_divisa = 0
dinero_a_cambiar = float(input("Cuanto dinero quieres cambiar:\n"))
divisa_original = input("Que divsa tienes?(pesos, dolares, euros):\n")

if divisa_original == "pesos":
    cambio_de_divisa = input("A que divisa quieres cambiar?(dolares, euros): \n")
    if cambio_de_divisa == "dolares":
        dinero_final = dinero_a_cambiar * peso_a_dolar
    elif cambio_de_divisa == "euros":
        dinero_final = dinero_a_cambiar * peso_a_euro
elif divisa_original == "dolares":
    cambio_de_divisa = input("A que divisa quieres cambiar?(pesos, euros):\n")
    if cambio_de_divisa == "pesos":
        dinero_final = dinero_a_cambiar * dolar_a_peso
    elif cambio_de_divisa == "euros":
        dinero_final = dinero_a_cambiar * dolar_a_euro
elif divisa_original == "euros":
        cambio_de_divisa = input("A que divisa quieres cambiar?(pesos, dolares)\n")
        if cambio_de_divisa == "pesos":
            dinero_final = dinero_a_cambiar * euro_a_peso
        elif cambio_de_divisa == "dolares":
            dinero_final = dinero_a_cambiar * euro_a_dolar

print("El cambio de {} {} es de {} {} ".format(dinero_a_cambiar, divisa_original, dinero_final, cambio_de_divisa))
