
Feature: Product purchase

  @smoke
  Scenario Outline: Product purchase
    Given the user successfully logs in using the username "<username>" and password "<password>"
    When the user selects the product to add to the shopping cart
    And goes to the shopping cart and checks out
    Then the user completes the checkout information using first name "<firstname>", last name "<lastname>" and postal code "<postalcode>"
    And finalizes the purchase order
    Examples:
      | username      | password     |  firstname | lastname | postalcode |
      | standard_user | secret_sauce |  julieta    | screpnik  | 5000     |
