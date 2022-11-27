from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")


class BasketPageLocators:
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//p[contains(text(), 'empty')]")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class MainPageLocators():
    pass


class ProductPageLocators:
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    ALERT_ADDED_TO_CART = (By.CSS_SELECTOR, "div.alertinner strong")
    ALERT_CART_STATUS = (By.CSS_SELECTOR, ".alert-noicon.alert-info p")
    ADDING_SUCCESS = (By.CSS_SELECTOR, "div.alert-success")
    PRICE_VALUE = (By.CLASS_NAME, "price_color")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
