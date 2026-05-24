Feature: No Size Selected

  Scenario: Add product without selecting size

    Given User launches Myntra website
    When User hovers on MEN menu
    And User opens Casual Shoes category
    And User opens first product
    And User clicks add to bag without size
    Then Size error message should display