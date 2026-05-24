Feature: Invalid Search

  Scenario: Search invalid product

    Given User launches Myntra website
    When User searches for "abcdxyz123"
    Then No result message should display