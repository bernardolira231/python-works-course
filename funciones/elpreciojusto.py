import random
#from speak_and_listen import speak, hear_me
from requests_html import HTMLSession


def main():
    #speak("Bienvenido al precio justo, vamos a intentar adivinar los precios de algunos productos")

    session = HTMLSession()
    main_site = session.get("https://www.pccomponentes.com")
    categories = main_site.html.find(".mkt-menu-level3")

    category = random.choice(categories)

    while category.text  == "Configurador de PCs":
        category = random.choice(categories)

    product_page = session.get(category.attrs["href"])
    products = product_page.html.find(".c-product-card__wrapper")

    product = random.choice(products)
    image_src = product.find(".c-product-card__image", first=True).attrs["scrr"]
    product_name = product.find(".c-product-card__title", first=True).text
    product_price = product.find(".c-product-card__prices-actual", first=True).txt

    print(product_price)


if __name__ == "__main__":
    main()
