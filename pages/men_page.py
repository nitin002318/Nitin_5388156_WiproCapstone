from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MenPage:

    def __init__(self, driver):

        self.driver = driver

        # MEN Menu
        self.men_menu = (
            By.XPATH,
            "//a[@data-group='men']"
        )

        # Casual Shoes Category
        self.casual_shoes = (
            By.XPATH,
            "//a[contains(@href,'casual-shoes')]"
        )

        # First Product
        self.first_product = (
            By.XPATH,
            "(//li[@class='product-base'])[1]"
        )

        # Add To Bag Button
        self.add_to_bag = (
            By.XPATH,
            "//div[contains(text(),'ADD TO BAG')]"
        )

        # GO TO BAG Button
        self.go_to_bag = (
            By.XPATH,
            "//span[contains(text(),'GO TO BAG')]"
        )

        # Bag Validation
        self.bag = (
            By.XPATH,
            "//div[contains(text(),'PRICE DETAILS')]"
        )

        # Donation Checkbox
        # self.donation_checkbox = (
        #     By.XPATH,
        #     "//label[contains(@for,'donation')]"
        # )

        # Total Amount
        # Total Amount
        self.total_amount = (
            By.XPATH,
            "//div[contains(@class,'priceDetail')]/span"
        )
        # Place Order Button
        self.place_order = (
            By.XPATH,
            "//div[contains(text(),'PLACE ORDER')]"
        )

    # Hover MEN
    def hover_on_men(self):

        actions = ActionChains(self.driver)

        men = self.driver.find_element(*self.men_menu)

        actions.move_to_element(men).perform()

    # Open Casual Shoes
    def click_casual_shoes(self):

        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.element_to_be_clickable(
                self.casual_shoes
            )
        ).click()

    # Open First Product
    def open_first_product(self):

        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.element_to_be_clickable(
                self.first_product
            )
        ).click()

        windows = self.driver.window_handles

        self.driver.switch_to.window(windows[1])

    # Select Dynamic Size
    def select_size(self, size):

        size_xpath = (
            f"//p[contains(text(),'{size}')]"
        )

        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, size_xpath)
            )
        ).click()

    # Add Product To Bag
    def add_product_to_bag(self):

        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.element_to_be_clickable(
                self.add_to_bag
            )
        ).click()

    # Open Cart Page
    def go_to_cart(self):

        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.element_to_be_clickable(
                self.go_to_bag
            )
        ).click()

    # Verify Bag
    def verify_bag(self):
        wait = WebDriverWait(self.driver, 20)

        return wait.until(
            EC.visibility_of_element_located(
                self.bag
            )
        ).is_displayed()

    # Get Total Amount
    # Get Total Amount
    def get_total_amount(self):
        wait = WebDriverWait(self.driver, 20)

        amounts = wait.until(
            EC.presence_of_all_elements_located(
                self.total_amount
            )
        )

        final_amount = amounts[-1].text

        final_amount = (
            final_amount.replace("₹", "")
            .replace(",", "")
            .strip()
        )

        return int(final_amount)

    # Select Donation Amount
    # Select Donation Amount
    def select_donation_amount(self, amount):
        wait = WebDriverWait(self.driver, 10)

        # Donation Button Dynamic XPath
        donation_xpath = (
            f"//div[@data-key='{amount}']"
        )

        donation_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, donation_xpath)
            )
        )

        # Scroll to Donation Button
        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            donation_button
        )

        # Click Donation Amount
        self.driver.execute_script(
            "arguments[0].click();",
            donation_button
        )
    # Click Place Order
    def click_place_order(self):

        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.element_to_be_clickable(
                self.place_order
            )
        ).click()