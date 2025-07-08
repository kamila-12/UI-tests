
import pytest
from pages.main_page import MainPage

def test_smoke(browser):
    main_page = MainPage(browser)

    browser.get("https://market.o.kg/")
    main_page.search()