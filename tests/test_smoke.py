
import pytest
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.profile_page import ProfilePage

def test_smoke(login_browser):
    browser = login_browser
    main_page = MainPage(browser)
    product_page = ProductPage(browser)
    profile_page = ProfilePage(browser)

    browser.get("https://market.o.kg/")

    # поиск iPhone 16
    main_page.search()

    # клик на карточку товара
    main_page.click_card()

    # добавление в избранные
    product_page.add_to_favorite()

    # Просмотр избранных в профиле
    product_page.click_profile()

    profile_page.go_to_favorities()


