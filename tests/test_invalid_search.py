import time

from utils.driver_setup import get_driver
from pages.men_page import MenPage
from utils.screenshot import take_screenshot
from utils.logger import logger


def test_invalid_search():

    print("Launching Myntra Website...")
    logger.info("Launching Myntra Website")

    driver = get_driver()

    driver.maximize_window()

    men = MenPage(driver)

    time.sleep(3)

    print("Searching Invalid Product...")
    logger.info("Searching Invalid Product: xyzabc123")
    men.search_product("xyzabc123")

    time.sleep(5)

    print("Verifying No Result Found...")
    logger.info("Verifying No Result Found")

    assert men.verify_invalid_search()

    take_screenshot(driver, "test_invalid_search")
    logger.info("Screenshot Captured")

    print("Negative Search Test Passed Successfully")
    logger.info("Negative Search Test Passed Successfully")

    time.sleep(5)

    driver.quit()
    logger.info("Browser Closed")