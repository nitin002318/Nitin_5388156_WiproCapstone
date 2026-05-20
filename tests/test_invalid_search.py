import time

from utils.driver_setup import get_driver
from pages.men_page import MenPage
from utils.screenshot import take_screenshot

def test_invalid_search():

    print("Launching Myntra Website...")

    driver = get_driver()

    driver.maximize_window()

    men = MenPage(driver)

    time.sleep(3)

    print("Searching Invalid Product...")
    men.search_product("xyzabc123")

    time.sleep(5)

    print("Verifying No Result Found...")

    assert men.verify_invalid_search()

    take_screenshot(driver, "invalid_search")

    print("Negative Search Test Passed Successfully")

    time.sleep(5)

    driver.quit()