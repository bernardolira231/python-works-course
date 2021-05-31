from time import sleep
from requests_html import HTMLSession

URL = "https://ddtech.mx/producto/tarjeta-de-video-nvidia-geforce-rtx-3070-8gb-evga-xc3-black-gaming-08g-p5-3751-kr-solo-1-pieza-por-cliente?id=8446"


def get_url(session):
    url_info = session.get(URL)
    return url_info


def buy_zone(url_info):
    buy_zone = url_info.html.find(".no-stock")
    return buy_zone


def main():
    session = HTMLSession()
    get_url(session)
    while True:
        if len(buy_zone(get_url(session))) == 0:
            print("Hay en existencia")
            break
        else:
            print("No hay en existencia")
        sleep(60)



if __name__ == '__main__':
    main()
