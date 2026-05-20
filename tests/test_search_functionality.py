import time

from utils.driver_setup import get_driver
from pages.men_page import MenPage
from utils.screenshot import take_screenshot


def test_search_functionality():

    print("Launching Myntra Website...")

    driver = get_driver()

    driver.maximize_window()

    men = MenPage(driver)

    time.sleep(3)

    print("Searching Sneakers...")
    men.search_product("Sneakers")

    time.sleep(5)

    print("Verifying Search Results...")

    assert men.verify_search_result()
    take_screenshot(driver, "search")


    time.sleep(3)

    print("Search Functionality Passed Successfully")

    time.sleep(5)

    driver.quit()