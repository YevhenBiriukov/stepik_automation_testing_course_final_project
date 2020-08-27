from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators
import time


class BasketPage(BasePage):
    def there_are_no_goods_in_the_basket(self):
        assert not self.is_not_element_present(*BasketPageLocators.GOODS_ARE_PRESENT_TEXT), \
            "Goods is presented, but should not be"

    def empty_basket_message_is_present(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE_TEXT), "Empty basket message text is not presented"

    # нужно попробовать добавить неявные ожидания и прогнать их с явными для предыдущего урока - просуммируется ли время?