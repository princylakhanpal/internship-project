# Created by lakha at 6/6/2025
Feature: Tests for Target Search


  Scenario: User can search for a product on Target
    Given Open Target main page
    When Search for tea
    Then Verify search worked


  Scenario: User can view their cart
    Given Open Target main page
    When Click on cart icon
    Then Verify cart is empty


  Scenario: User can sign in
    Given Open Target main page
    When Click on Account
    And Click Sign in button
    Then Verify Sign in page opened


  Scenario:   User can sign into their account
    Given Open Target main page
    When Click on Account
    And Click Sign in button
    And Input "auringonpistos@gmailot.com" in Email field
    And Click Continue button
    And Input "********" in Password field
    And Click Sign in with Password button
    Then Verify User is logged in