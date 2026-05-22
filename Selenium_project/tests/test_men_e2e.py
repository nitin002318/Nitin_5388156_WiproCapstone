import time
import pytest

from Selenium_project.utils.driver_setup import get_driver
from Selenium_project.pages import MenPage
from Selenium_project.utils.logger import logger
from Selenium_project.utils.csv_reader import get_test_data
from Selenium_project.utils.screenshot import take_screenshot


@pytest.mark.parametrize(
    "size, donation",
    get_test_data()
)
def test_men_e2e(size, donation):

    print("Launching Myntra Website...")
    logger.info("Launching Myntra Website")

    driver = get_driver()

    driver.maximize_window()

    men = MenPage(driver)

    time.sleep(3)

    # Hover MEN Menu
    print("Hovering on MEN menu...")
    logger.info("Hovering on MEN menu")

    men.hover_on_men()

    # Open Casual Shoes
    print("Opening Casual Shoes category...")
    logger.info("Opening Casual Shoes category")

    men.click_casual_shoes()

    # Open First Product
    print("Opening first product...")
    logger.info("Opening first product")

    men.open_first_product()

    # Select Size
    print(f"Selecting Size: {size}")
    logger.info(f"Selecting Size: {size}")

    men.select_size(size)

    # Add To Bag
    print("Adding product to bag...")
    logger.info("Adding product to bag")

    men.add_product_to_bag()

    # Open Cart
    print("Opening Cart Page...")
    logger.info("Opening Cart Page")

    men.go_to_cart()

    # Verify Product Added
    print("Verifying product in cart...")
    logger.info("Verifying product in cart")

    assert men.verify_bag()

    # Get Initial Amount
    initial_amount = men.get_total_amount()

    print(f"Initial Amount: {initial_amount}")
    logger.info(f"Initial Amount: {initial_amount}")

    # Select Donation
    print(f"Selecting Donation Amount: ₹{donation}")
    logger.info(f"Selecting Donation Amount: ₹{donation}")

    men.select_donation_amount(donation)

    time.sleep(2)

    # Get Final Amount
    final_amount = men.get_total_amount()

    print(f"Final Amount: {final_amount}")
    logger.info(f"Final Amount: {final_amount}")

    # Validate Donation Added
    assert final_amount > initial_amount

    # Screenshot
    take_screenshot(
        driver,
        f"e2e_{size}_{donation}"
    )

    logger.info("Screenshot Captured")

    print("Donation Added Successfully")
    logger.info("Donation Added Successfully")

    # Place Order
    print("Clicking Place Order...")
    logger.info("Clicking Place Order")

    men.click_place_order()

    print("E2E Test Passed Successfully")
    logger.info("E2E Test Passed Successfully")

    time.sleep(5)

    driver.quit()

    logger.info("Browser Closed")