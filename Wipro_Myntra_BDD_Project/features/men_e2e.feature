Feature: Myntra MEN Module

  Scenario: Complete MEN E2E Flow

    Given User launches Myntra website
    When User hovers on MEN menu
    And User opens Casual Shoes category
    And User opens first product
    And User selects size "8"
    And User adds product to bag
    And User opens cart page
    Then Product should be added to cart

    When User selects donation amount "10"
    Then Donation should be added successfully

    When User clicks place order
    Then E2E flow should complete successfully