import time

from utils.driver_setup import get_driver
from pages.men_page import MenPage


def test_no_size_selected():

    print("Launching Myntra Website...")

    driver = get_driver()

    driver.maximize_window()

    men = MenPage(driver)

    time.sleep(3)

    print("Hovering on MEN Menu...")
    men.hover_on_men()

    time.sleep(3)

    print("Opening Casual Shoes...")
    men.click_casual_shoes()

    time.sleep(5)

    print("Opening First Product...")
    men.open_first_product()

    time.sleep(5)

    print("Clicking Add To Bag Without Selecting Size...")
    men.add_product_to_bag()

    time.sleep(3)

    print("Verifying Error Message...")

    assert men.verify_size_error()

    print("Negative Test Passed Successfully")

    time.sleep(5)

    driver.quit()