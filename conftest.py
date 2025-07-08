import pytest
from selenium import webdriver
import pickle

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
@pytest.fixture
def login_browser(browser):
    browser.get("https://market.o.kg/")
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for c in cookies:
        browser.add_cookie(c)
    browser.refresh()
    return browser
