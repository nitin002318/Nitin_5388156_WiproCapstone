import time

from utils.driver_setup import get_driver
from pages.men_page import MenPage


def test_filter_functionality():

    print("Launching Myntra Website...")

    driver = get_driver()

    men = MenPage(driver)

    print("Hovering on MEN Menu...")
    men.hover_on_men()

    print("Opening Casual Shoes...")
    men.click_casual_shoes()

    print("Applying Puma Brand Filter...")
    men.apply_brand_filter()

    print("Verifying Filter Applied...")

    assert men.verify_filter_applied()

    print("Filter Functionality Passed Successfully")

    time.sleep(5)

    driver.quit()