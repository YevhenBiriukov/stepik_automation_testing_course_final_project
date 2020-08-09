from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_book_to_basket(self):
        add_book_to_basket_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_book_to_basket_button.click()
        assert True, "is not"