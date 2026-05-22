Feature: Sort Functionality

  Scenario: Apply Better Discount sort

    Given User launches Myntra website
    When User hovers on MEN menu
    And User opens Casual Shoes category
    And User clicks sort button
    And User selects Better Discount option
    Then Products should be sorted successfully