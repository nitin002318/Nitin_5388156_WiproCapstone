Feature: Search Functionality

  Scenario: Search valid product

    Given User launches Myntra website
    When User searches for "Sneakers"
    Then Search results should be displayed