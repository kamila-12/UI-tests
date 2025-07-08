from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.common.exceptions import StaleElementReferenceException

class ProductPage(BasePage):
    add_favorite_button = (By.CSS_SELECTOR, 'button.styled__FavoriteIconWrapper-sc-w4o5jn-0.ccYUNJ')
    favorites_icon = (By.CSS_SELECTOR, 'div.ProductHeader__HeaderActionsBlock-sc-1ihvb5s-0 > button')

    def add_to_favorite(self):
        for _ in range(3):
            try:
                WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable(self.add_favorite_button)
                ).click()
                break
            except StaleElementReferenceException:
                continue

