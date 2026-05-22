import time

from Selenium_project.utils.driver_setup import get_driver
from Selenium_project.pages import MenPage
from Selenium_project.utils.screenshot import take_screenshot
from Selenium_project.utils.logger import logger


def test_no_size_selected():

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

    print("Clicking Add To Bag Without Selecting Size...")
    logger.info("Clicking Add To Bag Without Selecting Size")
    men.add_product_to_bag()

    time.sleep(3)

    print("Verifying Error Message...")
    logger.info("Verifying Error Message")

    assert men.verify_size_error()

    take_screenshot(driver, "test_no_size_selected")
    logger.info("Screenshot Captured")

    print("Negative Test Passed Successfully")
    logger.info("Negative Test Passed Successfully")

    time.sleep(5)

    driver.quit()
    logger.info("Browser Closed")