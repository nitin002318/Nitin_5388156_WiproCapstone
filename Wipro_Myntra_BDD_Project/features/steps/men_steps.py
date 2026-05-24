from behave import *

from pages.men_page import MenPage


# =========================
# LAUNCH WEBSITE
# =========================

@given("User launches Myntra website")
def step_launch(context):

    context.men = MenPage(context.driver)

    context.men.open_website()


# =========================
# MEN MENU
# =========================

@when("User hovers on MEN menu")
def step_hover_men(context):

    context.men.hover_on_men()


# =========================
# CASUAL SHOES
# =========================

@when("User opens Casual Shoes category")
def step_open_casual(context):

    context.men.open_casual_shoes()


# =========================
# FIRST PRODUCT
# =========================

@when("User opens first product")
def step_open_product(context):

    context.men.open_first_product()


# =========================
# SIZE
# =========================

@when("User selects size")
def step_select_size(context):

    context.men.select_size()


# =========================
# ADD TO BAG
# =========================

@when("User adds product to bag")
def step_add_bag(context):

    context.men.add_product_to_bag()


# =========================
# OPEN CART
# =========================

@when("User opens cart page")
def step_open_cart(context):

    context.men.open_cart()


# =========================
# VERIFY CART
# =========================

@then("Product should be added successfully")
def step_verify_cart(context):

    assert context.men.verify_cart()


# =========================
# PLACE ORDER
# =========================

@when("User clicks place order")
def step_place_order(context):

    context.men.click_place_order()


# =========================
# VERIFY LOGIN PAGE
# =========================

@then("Login page should open")
def step_verify_login(context):

    assert context.men.verify_login_page()


# =========================
# SEARCH
# =========================

@when('User searches for "{product}"')
def step_search(context, product):

    context.men.search_product(product)


@then("Search results should be displayed")
def step_search_result(context):

    assert context.men.verify_search()


# =========================
# INVALID SEARCH
# =========================

@then("No result message should display")
def step_invalid_search(context):

    assert context.men.verify_invalid_search()


# =========================
# FILTER
# =========================

@when("User applies Puma filter")
def step_filter(context):

    context.men.apply_puma_filter()


@then("Puma filter should be applied")
def step_verify_filter(context):

    assert context.men.verify_filter()


# =========================
# SORT
# =========================

@when("User applies Better Discount sort")
def step_sort(context):

    context.men.apply_sort()


@then("Products should be sorted")
def step_verify_sort(context):

    assert context.men.verify_sort()


# =========================
# WISHLIST
# =========================

@when("User clicks wishlist button")
def step_wishlist(context):

    context.men.click_wishlist()


@then("Login popup should appear")
def step_verify_popup(context):

    assert context.men.verify_login_popup()


# =========================
# NO SIZE NEGATIVE
# =========================

@when("User clicks add to bag without size")
def step_add_without_size(context):

    context.men.add_product_to_bag()


@then("Size error message should display")
def step_verify_size_error(context):

    assert context.men.verify_size_error()