Feature: order_tanuki

  Scenario: test_order
    Given I navigate to the DC Home page
    When I login
    Then I see profile screen
    When I adding new address
    And Delete this address
    Then I see old address list
    Given I comeback to the DC Home Page
    When I input in search new address
    And Click by result vendors
    Then I see vendor-page
    When I order product
    And Open Basket
    And Open Checkout-Screen
    Then I see checkout

