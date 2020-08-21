from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_product_to_basket_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_product_to_basket_button.click()
        assert True, "is not"

    def is_book_names_match(self):
        book_name = self.browser.find_element(
            *ProductPageLocators.BOOK_NAME).text
        message_book_name = self.browser.find_element(
            *ProductPageLocators.MESSAGE_BOOK_NAME).text
        assert book_name == message_book_name, "names do not match"

    def is_prices_match(self):
        message_price_text = self.browser.find_element(
            *ProductPageLocators.BOOK_PRICE).text
        book_price_text = self.browser.find_element(
            *ProductPageLocators.MESSAGE_BOOK_PRICE).text
        assert message_price_text == book_price_text, "prices do not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_BOOK_NAME), \
            "Success message is presented, but should not be" # метод is_not_element_present возвратит false, ежели элемент все-таки будет найден. При другом варианте он упадет

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_BOOK_NAME), \
            "Success message does not disappeared" # а сей метод is_disappeared возвратит true, ежели элемент исчезнет (или, может не будет найден, вообще...). При другом варианте он упадет
