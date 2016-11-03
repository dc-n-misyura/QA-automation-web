Feature: Login
  # Login tests to cover login process.
  # Contains positive tests marked as [POSITIVE] tag and negative with [NEGATIVE] tag

  Scenario Outline: [POSITIVE] Successful login
    Given I open homepage
    And open header menu and click on login-registration link
    When I fill <email>, <password> and submit the form
    Then login was successful, check <name>

    Examples:
      | email | password | name |
      | w@w.com | 111111 | TEST! |
