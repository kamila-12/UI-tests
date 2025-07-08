from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class MainPage (BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    input_search = (By.CSS_SELECTOR, 'input[placeholder="Жарыяларды издөө"]')
    product_card = (By.ID, '6f64a01b-386b-4430-8a73-0028bd275767')


    def search(self):
        self.input(self.input_search, "iPhone 16\n")

    def click_card(self):
        (WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.product_card)
        )
         .click())



