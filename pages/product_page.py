from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from pages.base_page import BasePage

class ProductPage(BasePage):
    add_favorite_button = (By.CSS_SELECTOR, 'button.styled__FavoriteIconWrapper-sc-w4o5jn-0.ccYUNJ')

    def add_to_favorite(self):
        for _ in range(3):
            try:
                WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable(self.add_favorite_button)
                ).click()
                break
            except StaleElementReferenceException:
                continue

    def click_profile(self):
        for _ in range(3):
            try:
                WebDriverWait(self.browser, 15).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '//*[@id="__next"]/main/div/header/div[2]/div[2]/div[2]')
                    )
                ).click()
                break
            except StaleElementReferenceException:
                continue