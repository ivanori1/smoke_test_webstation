Feature: Login

  Scenario: Failed login
    Given Open WebStation login page
    When Click on Login button
    Then Error appears: "You have to accept the End User License Agreement in order to log in."