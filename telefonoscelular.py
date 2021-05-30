tu_telefono_sera = "No sabemos que puede ser de tu gusto"
ios_android = input("Quieres un IOS o un Android?:\n")

if ios_android == "android" or "Android" or "ANDROID":
    cantidad_de_dinero = input("Tienes dinero?:(S/N)\n")
    if cantidad_de_dinero == "S":
        camara_o_no = input("Te importa la camara?:(S/N)\n")
        if camara_o_no == "S":
            tu_telefono_sera = "Google Pixel Supercamara"
        elif camara_o_no == "N":
            tu_telefono_sera = "Android calidad-precio (Xiaomi)"
    elif cantidad_de_dinero == "N":
        tu_telefono_sera = "Android Chino $100"

elif ios_android == "IOS" or "ios" or "Ios":
    cantidad_de_dinero = input("Tienes dinero?:(S/N)\n")
    if cantidad_de_dinero == "S":
        tu_telefono_sera = "iPhone Ultra Pro Max"
    elif cantidad_de_dinero == "N":
        tu_telefono_sera = "iPhone segunda mano"
print("Segun tus gustos el mejor telefono para ti es un {}".format(tu_telefono_sera))
