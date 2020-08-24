import pytest
from .pages.product_page import ProductPage
import time
from .pages.login_page import LoginPage

# links = [
#     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                  marks=pytest.mark.xfail(reason="some bug")),
#     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                  marks=pytest.mark.xfail(reason="some bug")),
#     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                  marks=pytest.mark.xfail(reason="some bug")),
#     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                  marks=pytest.mark.xfail(reason="some bug")),
#     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                  marks=pytest.mark.xfail(reason="some bug")),
#     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                  marks=pytest.mark.xfail(reason="some bug")),
#     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                  marks=pytest.mark.xfail(reason="some bug")),
#     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                  marks=pytest.mark.xfail(reason="some bug")),
#     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                  marks=pytest.mark.xfail(reason="some bug")),
#     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
#                  marks=pytest.mark.xfail(reason="some bug")),
# ]


# @pytest.mark.parametrize('link', links)
# def test_guest_can_add_product_to_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_basket()
#     page.solve_quiz_and_get_code()
#     page.is_book_names_match()
#     page.is_prices_match()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()