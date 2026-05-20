from utils.driver_setup import get_driver
from pages.men_page import MenPage


def test_sort_functionality():

    print("Launching Myntra Website...")

    driver = get_driver()

    men = MenPage(driver)

    print("Hovering on MEN Menu...")
    men.hover_on_men()

    print("Opening Casual Shoes...")
    men.click_casual_shoes()

    print("Clicking Sort Button...")
    men.click_sort()

    print("Selecting Better Discount...")
    men.select_better_discount()

    print("Sort Functionality Test Passed Successfully")

    driver.quit()