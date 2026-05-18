from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class MenPage:

    def __init__(self, driver):
        self.driver = driver

        self.men_menu = (By.XPATH, "//a[@data-group='men']")

    def hover_on_men(self):

        actions = ActionChains(self.driver)

        men = self.driver.find_element(*self.men_menu)

        actions.move_to_element(men).perform()