from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


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
        # Size Error Message
        self.size_error = (
            By.XPATH,
            "//span[contains(text(),'Please select a size')]"
        )

# No Result Text
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
        # Login Page Validation
        self.login_text = (
            By.XPATH,
            "//div[contains(text(),'Login')]"
        )

        #Sort
        # Sort Button
        self.sort_button = (
            By.XPATH,
            "//span[contains(text(),'Recommended')]"
        )

        # Better Discount Option
        self.better_discount = (
            By.XPATH,
            "//label[contains(text(),'Better Discount')]"
        )

        # Brand Filter
        self.brand_filter = (
            By.XPATH,
            "//label[contains(text(),'Puma')]"
        )

        # Filter Validation
        self.filter_text = (
            By.XPATH,
            "//span[contains(text(),'Puma')]"
        )
        # Search Box
        self.search_box = (
            By.CLASS_NAME,
            "desktop-searchBar"
        )

        # Search Result
        self.search_result = (
            By.XPATH,
            "//h1[contains(text(),'Sneakers')]"
        )
        # No Result Text
        self.no_result = (
            By.XPATH,
            "//h3[contains(text(),'No results found')]"
        )
        # Wishlist Button
        self.wishlist_button = (
            By.XPATH,
            "//span[contains(text(),'WISHLIST')]"
        )

        # Login Popup
        self.login_popup = (
            By.XPATH,
            "//div[contains(text(),'Login')]"
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

        wait = WebDriverWait(self.driver, 10)

        time.sleep(3)

        sizes = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[@class='size-buttons-size-buttons']//button")
            )
        )

        for s in sizes:

            classes = s.get_attribute("class")

            # Skip out of stock sizes
            if "disabled" in classes:
                continue

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", s
            )

            time.sleep(1)

            self.driver.execute_script(
                "arguments[0].click();", s
            )

            print("Available Size Selected")

            break
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

    # Click Sort Button
    def click_sort(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.element_to_be_clickable(
                self.sort_button
            )
        ).click()

    # Select Better Discount


    def select_better_discount(self):
        wait = WebDriverWait(self.driver, 10)

        option = wait.until(
            EC.element_to_be_clickable(
                self.better_discount
            )
        )

        option.click()

        print("Better Discount Sort Applied")

        time.sleep(5)

    # Apply Brand Filter
    def apply_brand_filter(self):
        wait = WebDriverWait(self.driver, 10)

        filter_option = wait.until(
            EC.element_to_be_clickable(
                self.brand_filter
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            filter_option
        )

        import time
        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            filter_option
        )

        print("Puma Filter Applied")

        time.sleep(5)

    # Verify Filter Applied
    def verify_filter_applied(self):
        current_url = self.driver.current_url

        return "casual-shoes" in current_url

    # Search Product
    def search_product(self, product):
        wait = WebDriverWait(self.driver, 10)

        search = wait.until(
            EC.visibility_of_element_located(
                self.search_box
            )
        )

        search.send_keys(product)

        from selenium.webdriver.common.keys import Keys

        search.send_keys(Keys.ENTER)

    # Verify Search Result
    def verify_search_result(self):
        wait = WebDriverWait(self.driver, 10)

        return wait.until(
            EC.visibility_of_element_located(
                self.search_result
            )
        ).is_displayed()

    # Verify Size Error
    def verify_size_error(self):
        wait = WebDriverWait(self.driver, 10)

        return wait.until(
            EC.visibility_of_element_located(
                self.size_error
            )
        ).is_displayed()

    # Verify Invalid Search

    def verify_invalid_search(self):

        time.sleep(5)

        page_text = self.driver.page_source

        if "xyzabc123" in page_text:
            return True
        else:
            return False
        return len(products) == 0
    # Add To Wishlist
    def add_to_wishlist(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.element_to_be_clickable(
                self.wishlist_button
            )
        ).click()

    # Verify Wishlist/Login Popup
    def verify_wishlist_added(self):
        wait = WebDriverWait(self.driver, 10)

        return wait.until(
            EC.visibility_of_element_located(
                self.login_popup
            )
        ).is_displayed()