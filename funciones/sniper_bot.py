from time import sleep
from requests_html import HTMLSession
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

URL = "https://ddtech.mx/producto/tarjeta-de-video-nvidia-quadro-p400-v2-2gb-gddr5-pny-dp-mini-vcqp400v2-pb?id=7781"


def get_url_with_driver():
    driver = webdriver.Firefox()
    return driver


def get_url(session):
    url_info = session.get(URL)
    return url_info


def buy_zone(url_info):
    buy_zone = url_info.html.find(".no-stock")
    return buy_zone


def buy_button(driver):
    is_loaded = False
    while not is_loaded:
        try:
            driver.find_element_by_class_name("btn btn-primary add-cart").click()
            sleep(1)
            driver.find_element_by_class_name("messenger-close").click()
            driver.find_element_by_class_name("fa fa-shopping-cart").click()
            sleep(1)
            driver.find_element_by_id("terms").click()
            driver.find_element_by_class_name("btn btn-primary cart-checkout-btn").click()
            sleep(1)
            driver.find_element_by_id("email_login").click()
            driver.find_element_by_id("password_login").click()
        except NoSuchElementException:
            print("Intentando cargar nuevamente")


def main():
    session = HTMLSession()
    get_url(session)
    while True:
        if len(buy_zone(get_url(session))) == 0:
            print("Hay en existencia")
            buy_button(get_url_with_driver().get(URL))
            break
        else:
            print("No hay en existencia")
        sleep(60)


if __name__ == '__main__':
    main()
