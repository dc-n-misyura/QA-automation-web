Feature: User profile
  # User profile tests to cover profile-related functions.
  # Contains positive tests marked as [POSITIVE] tag and negative with [NEGATIVE] tag.

  Scenario Outline: [POSITIVE] Successful address addition
    Given I open homepage and login
    When I open user profile
    And enter <address> and submit the form
    Then I check that address has been added

    Examples:
      | address |
      | Москва, ул. Таганская, д. 30/2 |
