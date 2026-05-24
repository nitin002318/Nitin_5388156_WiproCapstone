import time

from Selenium_project.utils.driver_setup import get_driver
from Selenium_project.pages.men_page import MenPage
from Selenium_project.utils.screenshot import take_screenshot
from Selenium_project.utils.logger import logger


def test_search_functionality():

    print("Launching Myntra Website...")
    logger.info("Launching Myntra Website")

    driver = get_driver()
    driver.maximize_window()

    men = MenPage(driver)

    time.sleep(3)

    print("Searching Sneakers...")
    logger.info("Searching Sneakers")

    men.search_product("Sneakers")

    time.sleep(5)

    print("Verifying Search Results...")
    logger.info("Verifying Search Results")

    assert men.verify_search_result()

    take_screenshot(driver, "test_search_functionality")
    logger.info("Screenshot Captured")

    time.sleep(3)

    print("Search Functionality Passed Successfully")
    logger.info("Search Functionality Passed Successfully")

    time.sleep(5)

    driver.quit()
    logger.info("Browser Closed")