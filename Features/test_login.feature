

Feature: Login

  Scenario Outline: login with user and pass invalid
    Given I open the page
    When I enter username "<user>" and password "<password>"
    Then I should see the page "<results>"

    Examples:
      | user           | password          | results                  |
      | incorrectUser  | Password123       | Your username is invalid!|
      | student        | incorrectPassword | Your password is invalid!|


  Scenario Outline: login with user and pass valid
    Given I open a new page
    When I enter a valid username "<user>" and password "<password>"
    Then I should see the message "<results>"

    Examples:
      | user           | password          | results                  |
      | student        | Password123       | Logged In Successfully   |

