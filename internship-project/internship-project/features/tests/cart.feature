# Created by lakha at 6/10/2025
Feature: Cart Tests


  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open Target main page
    When Click on cart icon
    Then Verify 'Your cart is empty' message is shown
    Then Verify Cart page opened


  Scenario: User can add a product to cart
    Given Open Target main page
    When Search for mug
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item
    And Verify cart has correct product