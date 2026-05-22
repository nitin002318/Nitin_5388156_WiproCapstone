Feature: Invalid Search

  Scenario: Search invalid product

    Given User launches Myntra website
    When User searches invalid product
    Then No result message should be displayed