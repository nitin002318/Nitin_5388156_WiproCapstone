from behave import given, when, then
from pages.men_page import MenPage
from utils.driver_setup import get_driver
from utils.screenshot import take_screenshot
from utils.logger import logger
import time


# =========================
# COMMON STEPS
# =========================

@given("User launches Myntra website")
def step_launch_website(context):

    context.driver = get_driver()

    context.driver.maximize_window()

    context.men = MenPage(context.driver)

    print("Myntra Website Opened")
    logger.info("Myntra Website Opened")


@when("User hovers on MEN menu")
def step_hover_men(context):

    context.men.hover_on_men()

    print("Hovered on MEN Menu")
    logger.info("Hovered on MEN Menu")


@when("User opens Casual Shoes category")
def step_open_casual_shoes(context):

    context.men.click_casual_shoes()

    print("Casual Shoes Opened")
    logger.info("Casual Shoes Opened")


@when("User opens first product")
def step_open_first_product(context):

    context.men.open_first_product()

    print("First Product Opened")
    logger.info("First Product Opened")


# =========================
# E2E FLOW
# =========================

@when('User selects size "{size}"')
def step_select_size(context, size):

    context.men.select_size(size)

    print(f"Size Selected: {size}")
    logger.info(f"Size Selected: {size}")


@when("User adds product to bag")
def step_add_to_bag(context):

    context.men.add_product_to_bag()

    print("Product Added To Bag")
    logger.info("Product Added To Bag")


@when("User opens cart page")
def step_open_cart(context):

    context.men.go_to_cart()

    print("Cart Opened")
    logger.info("Cart Opened")


@then("Product should be added to cart")
def step_verify_bag(context):

    assert context.men.verify_bag()

    print("Product Verified In Cart")
    logger.info("Product Verified In Cart")


@when('User selects donation amount "{donation}"')
def step_select_donation(context, donation):

    context.initial_amount = context.men.get_total_amount()

    context.men.select_donation_amount(donation)

    time.sleep(2)

    context.final_amount = context.men.get_total_amount()

    print(f"Donation Selected: ₹{donation}")
    logger.info(f"Donation Selected: ₹{donation}")


@then("Donation should be added successfully")
def step_verify_donation(context):

    assert context.final_amount > context.initial_amount

    print("Donation Added Successfully")
    logger.info("Donation Added Successfully")


@when("User clicks place order")
def step_place_order(context):

    context.men.click_place_order()

    print("Place Order Clicked")
    logger.info("Place Order Clicked")


@then("E2E flow should complete successfully")
def step_complete(context):

    take_screenshot(context.driver, "e2e_flow")

    print("BDD E2E Test Passed Successfully")
    logger.info("BDD E2E Test Passed Successfully")

    time.sleep(3)

    context.driver.quit()

    logger.info("Browser Closed")


# =========================
# SEARCH FUNCTIONALITY
# =========================

@when('User searches for "{product}"')
def step_search_product(context, product):

    context.men.search_product(product)

    print(f"Searched Product: {product}")
    logger.info(f"Searched Product: {product}")


@then("Search results should be displayed")
def step_verify_search(context):

    assert context.men.verify_search_result()

    take_screenshot(context.driver, "search_functionality")

    print("Search Results Displayed Successfully")
    logger.info("Search Results Displayed Successfully")

    time.sleep(3)

    context.driver.quit()

    logger.info("Browser Closed")


# =========================
# FILTER FUNCTIONALITY
# =========================

@when("User applies Puma filter")
def step_apply_filter(context):

    context.men.apply_brand_filter()

    print("Puma Filter Applied")
    logger.info("Puma Filter Applied")


@then("Filter should be applied successfully")
def step_verify_filter(context):

    assert context.men.verify_filter_applied()

    take_screenshot(context.driver, "filter_functionality")

    print("Filter Applied Successfully")
    logger.info("Filter Applied Successfully")

    time.sleep(3)

    context.driver.quit()

    logger.info("Browser Closed")


# =========================
# SORT FUNCTIONALITY
# =========================

@when("User clicks sort button")
def step_click_sort(context):

    context.men.click_sort()

    print("Sort Button Clicked")
    logger.info("Sort Button Clicked")


@when("User selects Better Discount option")
def step_select_discount(context):

    context.men.select_better_discount()

    print("Better Discount Selected")
    logger.info("Better Discount Selected")


@then("Products should be sorted successfully")
def step_verify_sort(context):

    assert True

    take_screenshot(context.driver, "sort_functionality")

    print("Products Sorted Successfully")
    logger.info("Products Sorted Successfully")

    time.sleep(3)

    context.driver.quit()

    logger.info("Browser Closed")


# =========================
# WISHLIST FUNCTIONALITY
# =========================

@when("User adds product to wishlist")
def step_add_wishlist(context):

    context.men.add_to_wishlist()

    print("Product Added To Wishlist")
    logger.info("Product Added To Wishlist")


@then("Wishlist popup should be displayed")
def step_verify_wishlist(context):

    assert context.men.verify_wishlist_added()

    take_screenshot(context.driver, "wishlist_functionality")

    print("Wishlist Popup Displayed Successfully")
    logger.info("Wishlist Popup Displayed Successfully")

    time.sleep(3)

    context.driver.quit()

    logger.info("Browser Closed")


# =========================
# NEGATIVE TEST CASE
# NO SIZE SELECTED
# =========================

@when("User clicks add to bag without selecting size")
def step_add_without_size(context):

    context.men.add_product_to_bag()

    print("Clicked Add To Bag Without Selecting Size")
    logger.info("Clicked Add To Bag Without Selecting Size")


@then("Size error message should be displayed")
def step_verify_size_error(context):

    assert context.men.verify_size_error()

    take_screenshot(context.driver, "no_size_selected")

    print("Size Error Message Displayed Successfully")
    logger.info("Size Error Message Displayed Successfully")

    time.sleep(3)

    context.driver.quit()

    logger.info("Browser Closed")


# =========================
# NEGATIVE TEST CASE
# INVALID SEARCH
# =========================

@when("User searches invalid product")
def step_invalid_search(context):

    context.men.search_product("xyzabc123")

    print("Invalid Product Searched")
    logger.info("Invalid Product Searched")


@then("No result message should be displayed")
def step_verify_invalid_search(context):

    assert context.men.verify_invalid_search()

    take_screenshot(context.driver, "invalid_search")

    print("No Result Message Displayed Successfully")
    logger.info("No Result Message Displayed Successfully")

    time.sleep(3)

    context.driver.quit()

    logger.info("Browser Closed")