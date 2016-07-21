Scenario Outline: Order
  Given I navigate to the DC Home page and login
#  Открытие страницы логин, проверка профиля и обратно на главную
  When I input in search "<new_address>"
#  Ввожу адрес и попадаю в выдачу
  And Search and open "<vendor_title>"
#  Ищу необходимый ресторан через поиск и перехожу на страницу
  And Check vendor page
  # Проверяю корректность страницы ресторана
  When I make order
#  Формирую заказ больше минимальной суммы
  And Open cart and checkout
#  Проходим экран корзины и чекаута
  Then I have cart with order, phone and address
#  Открываем чекаут где сформирован заказ, с введённым адрессом, телефоном, - готовый к отправке

  Examples: New Address
  | new_address | vendor_title |
  | Москва, улица Александра Солженицына, 23Ас1 | Тануки |
  | Москва, улица Станиславского, 4 | Папа Джонс |
  | Москва, Пятницкая улица, 5 | Шампур Project |

Scenario: Registration New User
  Given Open home-page and open registration form
# Открываем главную страницу, далее открываем форму регистрации
  When Input all required fields "<username>", "<phone>", "<password>"
# Вводим все обязательные поля, - которые берутся из examples
  Then I press submit button and see homepage authorized user
# Нажимаем кнопку зарегистрироваться и видим главную страницу авторизованного пользователя

  Examples: Registration New User
  | username | phone | password |
  | test | 4444444444 | oisdhjkgfhj7362|
  | 2test | 4444444444 | sdjhfj7362|