from Selenium_project.utils.driver_setup import get_driver
from Selenium_project.pages import MenPage
from Selenium_project.utils.logger import logger
from Selenium_project.utils.screenshot import take_screenshot

def test_sort_functionality():

    # logger = setup_logger()

    print("Launching Myntra Website...")
    logger.info("Launching Myntra Website...")

    driver = get_driver()

    men = MenPage(driver)

    print("Hovering on MEN Menu...")
    logger.info("Hovering on MEN Menu...")

    men.hover_on_men()

    print("Opening Casual Shoes...")
    logger.info("Opening Casual Shoes...")

    men.click_casual_shoes()

    print("Clicking Sort Button...")
    logger.info("Clicking Sort Button...")

    men.click_sort()

    print("Selecting Better Discount...")
    logger.info("Selecting Better Discount...")

    men.select_better_discount()
    take_screenshot(driver, "test_sort_functionality")

    print("Sort Functionality Passed Successfully")
    logger.info("Sort Functionality Passed Successfully")

    driver.quit()