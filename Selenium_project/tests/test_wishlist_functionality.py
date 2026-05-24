import time

from Selenium_project.utils.driver_setup import get_driver
from Selenium_project.pages.men_page import MenPage
from Selenium_project.utils.screenshot import take_screenshot
from Selenium_project.utils.logger import logger


def test_wishlist_functionality():

    print("Launching Myntra Website...")
    logger.info("Launching Myntra Website")

    driver = get_driver()
    driver.maximize_window()

    men = MenPage(driver)

    time.sleep(3)

    print("Hovering on MEN Menu...")
    logger.info("Hovering on MEN Menu")

    men.hover_on_men()

    time.sleep(3)

    print("Opening Casual Shoes...")
    logger.info("Opening Casual Shoes")

    men.click_casual_shoes()

    time.sleep(5)

    print("Opening First Product...")
    logger.info("Opening First Product")

    men.open_first_product()

    time.sleep(5)

    print("Adding Product To Wishlist...")
    logger.info("Adding Product To Wishlist")

    men.add_to_wishlist()

    time.sleep(5)

    print("Verifying Wishlist Added...")
    logger.info("Verifying Wishlist Added")

    assert men.verify_wishlist_added()

    take_screenshot(driver, "test_wishlist_functionality")
    logger.info("Screenshot Captured")

    print("Wishlist Test Passed Successfully")
    logger.info("Wishlist Test Passed Successfully")

    time.sleep(5)

    driver.quit()
    logger.info("Browser Closed")