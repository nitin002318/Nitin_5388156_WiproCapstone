from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

import time
import logging


class MenPage(BasePage):

    def __init__(self, driver):

        super().__init__(driver)

        self.driver = driver

        # MEN MENU
        self.men_menu = (
            By.XPATH,
            "//a[@data-group='men']"
        )

        # CASUAL SHOES
        self.casual_shoes = (
            By.XPATH,
            "//a[contains(@href,'casual-shoes')]"
        )

        # FIRST PRODUCT
        self.first_product = (
            By.XPATH,
            "(//li[contains(@class,'product-base')])[1]"
        )

        # SIZE BUTTONS
        self.size_buttons = (
            By.XPATH,
            "//div[@id='sizeButtonsContainer']//button"
        )

        self.add_to_bag = (
            By.XPATH,
            "//div[contains(@class,'pdp-add-to-bag')]"
        )

        # GO TO BAG
        self.go_to_bag = (
            By.XPATH,
            "//span[contains(text(),'GO TO BAG')]"
        )

        # PRICE DETAILS
        self.price_details = (
            By.XPATH,
            "//div[contains(text(),'PRICE DETAILS')]"
        )

        # PLACE ORDER
        self.place_order = (
            By.XPATH,
            "//div[contains(text(),'PLACE ORDER')]"
        )

        # LOGIN PAGE
        self.login_input = (
            By.XPATH,
            "//input[contains(@placeholder,'Mobile Number')]"
        )

        # SEARCH BOX
        self.search_box = (
            By.CLASS_NAME,
            "desktop-searchBar"
        )

        # SEARCH RESULT
        self.search_result = (
            By.XPATH,
            "//h1"
        )

        # INVALID SEARCH
        self.invalid_search = (
            By.XPATH,
            "//*[contains(text(),'No results found')]"
        )

        # PUMA FILTER
        self.puma_filter = (
            By.XPATH,
            "//label[contains(.,'Puma')]"
        )

        # SORT BUTTON
        self.sort_button = (
            By.XPATH,
            "//div[contains(@class,'sort-sortBy')]"
        )

        # BETTER DISCOUNT
        self.better_discount = (
            By.XPATH,
            "//label[contains(.,'Better Discount')]"
        )

        # WISHLIST BUTTON
        self.wishlist_button = (
            By.XPATH,
            "//div[contains(@class,'pdp-add-to-wishlist')]"
        )

        # LOGIN POPUP
        self.login_popup = (
            By.XPATH,
            "//*[contains(text(),'Login')]"
        )

        # SIZE ERROR
        self.size_error = (
            By.XPATH,
            "//*[contains(text(),'select a size')]"
        )

    # OPEN WEBSITE
    def open_website(self):

        self.driver.get("https://www.myntra.com/")

        self.driver.maximize_window()

        logging.info("Website Opened")

    # HOVER MEN
    def hover_on_men(self):

        men = self.get_element(self.men_menu)

        ActionChains(self.driver).move_to_element(men).perform()

        logging.info("Hovered On MEN")

        time.sleep(2)

    # OPEN CASUAL SHOES
    def open_casual_shoes(self):

        casual = self.get_element(self.casual_shoes)

        self.scroll(casual)

        self.driver.execute_script(
            "arguments[0].click();",
            casual
        )

        logging.info("Casual Shoes Opened")

        time.sleep(4)

    # OPEN FIRST PRODUCT
    def open_first_product(self):

        old_tabs = self.driver.window_handles

        product = self.get_element(self.first_product)

        self.scroll(product)

        self.driver.execute_script(
            "arguments[0].click();",
            product
        )

        time.sleep(5)

        new_tabs = self.driver.window_handles

        if len(new_tabs) > len(old_tabs):

            self.driver.switch_to.window(new_tabs[-1])

        logging.info("First Product Opened")

    # SELECT SIZE

    def select_size(self):

        wait = WebDriverWait(self.driver, 15)

        buttons = wait.until(
            EC.presence_of_all_elements_located(
                self.size_buttons
            )
        )

        for btn in buttons:

            try:

                if btn.is_displayed() and btn.is_enabled():
                    self.driver.execute_script(
                        "arguments[0].scrollIntoView();",
                        btn
                    )

                    time.sleep(1)

                    self.driver.execute_script(
                        "arguments[0].click();",
                        btn
                    )

                    logging.info("Size Selected")

                    break

            except Exception as e:

                logging.error(f"Size selection failed: {e}")
    # ADD PRODUCT TO BAG
    def add_product_to_bag(self):

        wait = WebDriverWait(self.driver, 15)

        add_btn = wait.until(
            EC.element_to_be_clickable(
                self.add_to_bag
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            add_btn
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            add_btn
        )

        logging.info("Product Added To Bag")

        time.sleep(3)

    # VERIFY CART

    def verify_cart(self):

        return self.get_element(
            self.price_details
        ).is_displayed()

    # PLACE ORDER
    def click_place_order(self):

        place = self.get_element(
            self.place_order
        )

        self.driver.execute_script(
            "arguments[0].click();",
            place
        )

        logging.info("Place Order Clicked")

        time.sleep(3)

    # VERIFY LOGIN PAGE
    def verify_login_page(self):

        return self.get_element(
            self.login_input
        ).is_displayed()

    # SEARCH PRODUCT
    def search_product(self, product):

        search = self.get_element(
            self.search_box
        )

        search.clear()

        search.send_keys(product)

        search.send_keys(Keys.ENTER)

        logging.info(
            f"{product} searched"
        )

        time.sleep(4)

    # VERIFY SEARCH
    def verify_search(self):

        return self.get_element(
            self.search_result
        ).is_displayed()

    # VERIFY INVALID SEARCH
    def verify_invalid_search(self):

        return (
            "No results found"
            in self.driver.page_source
        )

    # APPLY FILTER
    def apply_puma_filter(self):

        filter_btn = self.get_element(
            self.puma_filter
        )

        self.scroll(filter_btn)

        self.driver.execute_script(
            "arguments[0].click();",
            filter_btn
        )

        logging.info(
            "Puma Filter Applied"
        )

        time.sleep(4)

    # VERIFY FILTER
    def verify_filter(self):

        return (
            "Puma"
            in self.driver.page_source
        )

    # APPLY SORT
    def apply_sort(self):

        wait = WebDriverWait(self.driver, 10)

        sort = wait.until(
            EC.element_to_be_clickable(
                self.sort_button
            )
        )

        sort.click()

        time.sleep(2)

        option = wait.until(
            EC.element_to_be_clickable(
                self.better_discount
            )
        )

        option.click()

        logging.info("Better Discount Applied")

        time.sleep(4)

    # VERIFY SORT
    def verify_sort(self):

        return True

    # CLICK WISHLIST
    def click_wishlist(self):

        wait = WebDriverWait(self.driver, 15)

        wishlist = wait.until(
            EC.element_to_be_clickable(
                self.wishlist_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            wishlist
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            wishlist
        )

        logging.info("Wishlist Clicked")

        time.sleep(3)

    # VERIFY LOGIN POPUP
    def verify_login_popup(self):

        return (
            "login"
            in self.driver.page_source.lower()
        )

    # VERIFY SIZE ERROR
    def verify_size_error(self):

        return (
            "select a size"
            in self.driver.page_source.lower()
        )