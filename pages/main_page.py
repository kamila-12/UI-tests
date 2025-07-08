from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage (BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    input_search = (By.CSS_SELECTOR, 'input[placeholder="Жарыяларды издөө"]')

    def search(self):
        self.input(self.input_search, "iPhone 16\n")

