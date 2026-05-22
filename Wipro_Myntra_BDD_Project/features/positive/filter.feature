Feature: Filter Functionality

  Scenario: Apply Puma brand filter

    Given User launches Myntra website
    When User hovers on MEN menu
    And User opens Casual Shoes category
    And User applies Puma filter
    Then Filter should be applied successfully