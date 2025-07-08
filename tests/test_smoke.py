
import pytest
from pages.main_page import MainPage
from pages.product_page import ProductPage


def test_smoke(login_browser):
    browser = login_browser
    main_page = MainPage(browser)
    product_page = ProductPage(browser)

    browser.get("https://market.o.kg/")

    # поиск iPhone 16
    main_page.search()

    # клик на карточку товара
    main_page.click_card()

    # добавление в избранные
    product_page.add_to_favorite()


