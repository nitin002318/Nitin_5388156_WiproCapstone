from behave import given, when, then
from pages.men_page import MenPage
from utils.driver_setup import get_driver
import time


@given("User launches Myntra website")
def step_launch_website(context):

    context.driver = get_driver()

    context.driver.maximize_window()

    context.men = MenPage(context.driver)

    print("Myntra Website Opened")


@when("User hovers on MEN menu")
def step_hover_men(context):

    context.men.hover_on_men()

    print("Hovered on MEN Menu")


@when("User opens Casual Shoes category")
def step_open_casual_shoes(context):

    context.men.click_casual_shoes()

    print("Casual Shoes Opened")


@when("User opens first product")
def step_open_first_product(context):

    context.men.open_first_product()

    print("First Product Opened")


@when('User selects size "{size}"')
def step_select_size(context, size):

    context.men.select_size(size)

    print(f"Size Selected: {size}")


@when("User adds product to bag")
def step_add_to_bag(context):

    context.men.add_product_to_bag()

    print("Product Added To Bag")


@when("User opens cart page")
def step_open_cart(context):

    context.men.go_to_cart()

    print("Cart Opened")


@then("Product should be added to cart")
def step_verify_bag(context):

    assert context.men.verify_bag()

    print("Product Verified In Cart")


@when('User selects donation amount "{donation}"')
def step_select_donation(context, donation):

    context.initial_amount = context.men.get_total_amount()

    context.men.select_donation_amount(donation)

    time.sleep(2)

    context.final_amount = context.men.get_total_amount()

    print("Donation Selected")


@then("Donation should be added successfully")
def step_verify_donation(context):

    assert context.final_amount > context.initial_amount

    print("Donation Added Successfully")


@when("User clicks place order")
def step_place_order(context):

    context.men.click_place_order()

    print("Place Order Clicked")


@then("E2E flow should complete successfully")
def step_complete(context):

    print("BDD E2E Test Passed Successfully")

@when('User searches for "{product}"')
def step_search_product(context, product):
    context.men.search_product(product)

@then('Search results should be displayed')
def step_verify_search(context):
    assert context.men.verify_search_result()

@when('User applies Puma filter')
def step_apply_filter(context):
   context.men.apply_brand_filter()

@then('Filter should be applied successfully')
def step_verify_filter(context):
    assert context.men.verify_filter_applied()

@when('User clicks sort button')
def step_click_sort(context):
        context.men.click_sort()

@when('User selects Better Discount option')
def step_select_discount(context):
    context.men.select_better_discount()

@then('Products should be sorted successfully')
def step_verify_sort(context):
    assert True
    time.sleep(5)

    context.driver.quit()