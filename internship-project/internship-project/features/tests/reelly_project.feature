# Created by lakha at 7/16/2025
Feature: Tests to verify upload image and next buttons available

  Scenario: User can click on verifications settings option and verify the right page opens
     Given Open the main page
     When Enter princygulati@yahoo.com into email
      And Enter princy123 into password
      And Click continue button
      And Click on settings at the left side menu
      And Click on the verification option
     Then Verify the right page opens