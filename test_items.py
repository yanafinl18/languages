import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_be_basket_button(browser):
    browser.get(link)
    time.sleep(10)
    btn_to_add_basket = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert btn_to_add_basket, "Кнопка добавления в корзину отсутствует на странице"
