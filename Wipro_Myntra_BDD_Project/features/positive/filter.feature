Feature: Filter Functionality

  Scenario: Apply Puma Filter

    Given User launches Myntra website
    When User hovers on MEN menu
    And User opens Casual Shoes category
    And User applies Puma filter
    Then Puma filter should be applied