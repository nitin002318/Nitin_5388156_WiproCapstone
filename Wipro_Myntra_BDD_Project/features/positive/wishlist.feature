Feature: Wishlist Functionality

  Scenario: Add product to wishlist

    Given User launches Myntra website
    When User hovers on MEN menu
    And User opens Casual Shoes category
    And User opens first product
    And User adds product to wishlist
    Then Wishlist popup should be displayed