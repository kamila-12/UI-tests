from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class ProfilePage(BasePage):
    favorities_tab = (By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div[1]/div/div/div[2]')

    def go_to_favorities(self):
        for _ in range(3):
            try:
                WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable(self.favorities_tab)
                ).click()
                break
            except StaleElementReferenceException:
                continue
