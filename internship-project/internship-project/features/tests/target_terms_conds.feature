# Created by lakha at 6/25/2025
Feature: Tests for Target Sign in page


  Scenario:  User can open and close Terms and Conditions from sign in page
    Given Open sign in page
    When Store original window
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And Close new window
    And Return to original window