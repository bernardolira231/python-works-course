import requests
from requests_html import HTMLSession

URL = "https://ddtech.mx/producto/tarjeta-de-video-nvidia-geforce-rtx-3070-8gb-evga-xc3-black-gaming-08g-p5-3751-kr-solo-1-pieza-por-cliente?id=8446"


def buy_zone(session):
    buy_zone = session.html.find("#btnsWishAddBuy")
    return buy_zone


def main():
    session = HTMLSession()
    buy_zone(session)
    if len(buy_zone) > 0:
        print("Hay en existencia")



if __name__ == '__main__':
    main()
