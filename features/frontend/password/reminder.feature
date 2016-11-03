#noinspection CucumberUndefinedStep
Feature: Password reminder
  Scenario: [NEGATIVE] Submit form with empty fields
    Given I open homepage
    And I open header menu
    And click on link Забыли пароль?
    When I submit form
    Then I see error message Введите Ваш Е-mail который Вы указали при регистрации.

#  Scenario: Submit incorrect e-mail
#    Given I open homepage
#    And click on link Забыли пароль?
#    When I open header menu
#    And enter invalid email
#    And I click on button Войти
#    Then I see error message Поле «Электронная почта» заполнено некорректно
#
#  Scenario: Submit incorrect e-mail
#    Given I open homepage
#    When I open header menu
#    And enter invalid email
#    And I click on button Войти
#    Then I see error message Поле «Электронная почта» заполнено некорректно
