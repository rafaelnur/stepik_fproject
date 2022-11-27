from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART).click()

    def should_be_message_about_adding(self) -> None:
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_NAME), "Product name is not present"
        assert self.is_element_present(
            *ProductPageLocators.ALERT_ADDED_TO_CART
        ), "No alert that a product has been added to cart"
        alert_text = self.browser.find_element(
            *ProductPageLocators.ALERT_ADDED_TO_CART).text
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        assert product_name == alert_text, \
            f"The alert contains wrong product name: {alert_text} - {product_name}"

    def should_be_message_basket_total(self) -> None:
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_PRICE), "Product price is not present"
        assert self.is_element_present(*ProductPageLocators.ALERT_CART_STATUS
                                       ), "No alert with cart status"
        alert_text = self.browser.find_element(
            *ProductPageLocators.ALERT_CART_STATUS).text.split()[-1]
        product_cost = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text
        assert product_cost == alert_text, \
            f"Product cost in cart is not equal to the product cost {alert_text} != {product_cost}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDING_SUCCESS), \
            "Success element is visible for an user"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADDING_SUCCESS), "Success message has not disappeared"


