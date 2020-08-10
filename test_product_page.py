import pytest
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

# Ниже должен быть вызов следующих методов:
#     Метод проверки 1-ого ожидаемого результата (описанный в product_page.py - с двумя assert)
#     Метод проверки 2-ого ожидаемого результата (описанный в product_page.py - с двумя assert)
