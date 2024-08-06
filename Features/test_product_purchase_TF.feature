
Feature: Product purchase


  Scenario Outline: Product purchase
    Given the user successfully logs in using the username "<username>" and password "<password>"
    When the user selects the product named "<product_name>" to add to the shopping cart
    And goes to the shopping cart and checks out
    Then the user completes the checkout information using first name "<first_name>", last name "<last_name>" and postal code "<postal_code>"
    And finalizes the purchase order
    Examples:
      | username      | password     | product_name        | first_name | last_name | postal_code |
      | standard_user | secret_sauce | Sauce Labs Backpack | Julieta    | Screpnik  | 5000        |
