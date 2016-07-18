from model.group import Login


def test_order(app):
    app.open_home_page()
    app.session.login(Login(login="w@w.com",password="111111"))
    app.assert_title_profile()
    app.assert_balls()
    app.add_new_address(new_address="Москва, улица Александра Солженицына, 23Ас1")
    app.delete_first_address()
    app.open_home_page()
    app.find_by_address_from_home_page(new_address="Москва, улица Александра Солженицына, 23Ас4")
    app.open_vendor_from_search(title="Тануки")
    app.assert_vendor_page()
    app.ordering_products()
    app.open_cart()
    app.open_checkout()
    app.assert_checkout()
    app.destroy()




