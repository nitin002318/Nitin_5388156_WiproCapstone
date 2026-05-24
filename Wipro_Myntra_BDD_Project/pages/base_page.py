from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 15)

    def get_element(self, locator):

        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def get_elements(self, locator):

        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    def scroll(self, element):

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            element
        )