Scenario Outline: Order
  Given I navigate to the DC Home page and login
#  Открытие страницы логин, проверка профиля и обратно на главную
  When I input in search new address, search vendor, open him, and make order
#  Вводим адресс, с помощью поиска находим ресторан, формируем заказ
  Then I have cart with order, phone and address
#  Открываем чекаут где сформирован заказ, с введённым адрессом, телефоном, - готовый к отправке










#  When I adding new address
#  When Delete this address
#  Then I see old address list
#  Given I comeback to the DC Home Page
#  When I input in search new address
#  Given Click by result vendors
#  Then I see vendor-page
#  Given I order product
#  Then Open Basket
#  Given Open Checkout-Screen
#  Then I see checkout