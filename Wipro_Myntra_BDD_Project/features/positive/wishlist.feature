Feature: Wishlist Functionality

  Scenario: Add Product To Wishlist

    Given User launches Myntra website
    When User hovers on MEN menu
    And User opens Casual Shoes category
    And User opens first product
    And User clicks wishlist button
    Then Login popup should appear