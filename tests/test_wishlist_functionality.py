import time

from utils.driver_setup import get_driver
from pages.men_page import MenPage
from utils.screenshot import take_screenshot



def test_wishlist_functionality():

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

    print("Adding Product To Wishlist...")
    men.add_to_wishlist()

    time.sleep(5)

    print("Verifying Wishlist Added...")

    assert men.verify_wishlist_added()
    take_screenshot(driver, "WIshlist")


    print("Wishlist Test Passed Successfully")

    time.sleep(5)

    driver.quit()