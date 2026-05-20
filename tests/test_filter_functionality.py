import time

from utils.driver_setup import get_driver
from pages.men_page import MenPage
from utils.screenshot import take_screenshot
from utils.logger import logger


def test_filter_functionality():

    print("Launching Myntra Website...")
    logger.info("Launching Myntra Website")

    driver = get_driver()

    men = MenPage(driver)

    print("Hovering on MEN Menu...")
    logger.info("Hovering on MEN Menu")
    men.hover_on_men()

    print("Opening Casual Shoes...")
    logger.info("Opening Casual Shoes")
    men.click_casual_shoes()

    print("Applying Puma Brand Filter...")
    logger.info("Applying Puma Brand Filter")
    men.apply_brand_filter()

    print("Verifying Filter Applied...")
    logger.info("Verifying Filter Applied")

    assert men.verify_filter_applied()

    take_screenshot(driver, "Filter_applied")
    logger.info("Screenshot Captured")

    print("Filter Functionality Passed Successfully")
    logger.info("Filter Functionality Passed Successfully")

    time.sleep(5)

    driver.quit()
    logger.info("Browser Closed")