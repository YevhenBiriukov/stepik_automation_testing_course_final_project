import pytest
from .pages.product_page import ProductPage
import time

links = [
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/",
                 marks=pytest.mark.xfail(reason="some bug")),
]

@pytest.mark.xfail(reason="fixing this bug right now")
@pytest.mark.parametrize('link', links)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="fixing this bug right now")
@pytest.mark.parametrize('link', links)
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="fixing this bug right now")
@pytest.mark.parametrize('link', links)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.success_message_is_disappeared()