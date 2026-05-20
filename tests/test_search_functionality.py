import time

from utils.driver_setup import get_driver
from pages.men_page import MenPage


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

    time.sleep(3)

    print("Search Functionality Passed Successfully")

    time.sleep(5)

    driver.quit()