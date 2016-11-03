Feature: Registration
  # Registration tests to cover registration process.
  # Contains positive tests marked as [POSITIVE] tag and negative with [NEGATIVE] tag.



  Scenario Outline: [POSITIVE] Successful registration
    Given I open homepage
    And open header menu and click on registration link
    When I fill <name>, <phone>, email, <password> and submit the form
    Then registration was successful with <name>

    Examples:
      | name | phone | password |
      | Владимир | 4449190912 | Pas2sW0rd3 |


  Scenario: [NEGATIVE] Error message when fields are empty and uncheck user agreement
    Given I open homepage and open registration form
    When I click on the checkbox User Agreement to uncheck it
    And I click on submit form button
    Then I see error message



  Scenario Outline: [NEGATIVE] The absence checkbox of the user agreement
    Given I open homepage and open registration form
    When I input <name>, <phone>, <mail>, <password>
    And I click on the checkbox User Agreement to uncheck it
    And I click on submit form button
    Then I see error message

    Examples:
    | name | phone | mail | password |
    | TEST123 | 4449190912 | klok@list.ru | qwe@W#wq |


  Scenario Outline: [NEGATIVE] Incorrect format phone number
    Given Open home-page and open registration form
    When I input <name>, <incorrectphone>, <email>, <password>
    Then I press submit button and see all error-message
    And I see red phone field

    Examples:
    | name | incorrectphone | email | password |
    | TEST123 | 444919 | klok@ya.ru | qwe@W#wq |