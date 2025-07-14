# Created by lakha at 6/11/2025
Feature: Tests to verify Target help UI elements


  Scenario: Verify help page has correct amount of UI elements
    Given Open Target help page
    Then Verify Help page has main header
    And Verify Help page has search input
    And Verify Help page has footer section
    And Verify Help page has search boxes
