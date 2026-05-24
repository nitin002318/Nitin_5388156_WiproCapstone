Feature: Myntra MEN E2E Flow

  Scenario: Complete MEN Module Flow

    Given User launches Myntra website
    When User hovers on MEN menu
    And User opens Casual Shoes category
    And User opens first product
    And User selects size
    And User adds product to bag
    And User opens cart page
    Then Product should be added successfully

    When User clicks place order
    Then Login page should open