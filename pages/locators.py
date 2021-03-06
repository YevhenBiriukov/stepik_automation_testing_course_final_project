from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_PAGE_LINK = (By.CSS_SELECTOR, "span a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    GOODS_ARE_PRESENT_TEXT = (By.CSS_SELECTOR, ".row col-sm-6")
    EMPTY_BASKET_MESSAGE_TEXT = (By.CSS_SELECTOR, "#content_inner p a")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_INPUT2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    MESSAGE_BOOK_NAME = (By.CSS_SELECTOR, ".alertinner > strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    MESSAGE_BOOK_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")
