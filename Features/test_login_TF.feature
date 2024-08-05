
Feature: Positive Login test

  @smoke
  Scenario Outline: Positive Login test
    Given the user is on the login page
    When the user types the username "<username>" and password "<password>"
    Then shows home page
    Examples:
      | username      | password     |
      | standard_user | secret_sauce |
