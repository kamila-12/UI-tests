class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, locator):
        return self.browser.find_element(*locator)

    def click(self, locator):
        self.find(locator).click()

    def input(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)