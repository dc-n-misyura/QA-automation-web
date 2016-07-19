Scenario Outline: Order
  Given I navigate to the DC Home page and login
#  Открытие страницы логин, проверка профиля и обратно на главную
  When I input in search new address
#  Ввожу адрес и попадаю в выдачу
  And Search and open vendor
#  Ищу необходимый ресторан через поиск и перехожу на страницу
  And Check vendor page
  # Проверяю корректность страницы ресторана
  When I make order
#  Формирую заказ больше минимальной суммы
  And Open cart and checkout
#  Проходим экран корзины и чекаута
  Then I have cart with order, phone and address
#  Открываем чекаут где сформирован заказ, с введённым адрессом, телефоном, - готовый к отправке