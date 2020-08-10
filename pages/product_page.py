from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_product_to_basket_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON)
        time.sleep(3)
        add_product_to_basket_button.click()
        assert True, "is not"
