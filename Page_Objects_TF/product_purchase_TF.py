from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from Page_Objects_TF.page_base_TF import BasePageTF


class ProductPageTF(BasePageTF):
    _product_locator = (By.XPATH, "//DIV[@class='inventory_item_name '][text()='Sauce Labs Backpack']")
    _button_add_to_cart = (By.XPATH, "//BUTTON[@id='add-to-cart-sauce-labs-backpack']")
    _shopping_cart = (By.XPATH, "//A[@class='shopping_cart_link']")
    _cart_item = (By.XPATH, "//DIV[@class='inventory_item_name'][text()='Sauce Labs Backpack']")
    _checkout_button = (By.XPATH, "//button[@id='checkout']")
    _checkout_title = (By.XPATH, "//SPAN[@class='title'][text()='Checkout: Your Information']")
    _first_name_locator = (By.XPATH, "//INPUT[@id='first-name']")
    _last_name_locator = (By.XPATH, "//INPUT[@id='last-name']")
    _postal_code_locator = (By.XPATH, "//INPUT[@id='postal-code']")
    _continue_button = (By.XPATH, "//input[@id='continue']")
    _checkout_overview = (By.XPATH, "//SPAN[@class='title'][text()='Checkout: Overview']")
    _payment_information = (By.XPATH, "//DIV[@class='summary_info_label'][text()='Payment Information:']")
    _finish_button = (By.ID, "finish")
    _cart_title = (By.XPATH, "//SPAN[@class='title'][text()='Your Cart']")
    _message_complete_order = (By.XPATH, "//H2[@class='complete-header'][text()='Thank you for your order!']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def product_displayed(self) -> bool:
        super()._wait_until_element_is_visible(self._product_locator, 10)
        return super()._is_displayed(self._product_locator)

    def select_product(self):
        super()._click(self._button_add_to_cart)

    def go_to_shopping_cart(self) -> bool:
        super()._click(self._shopping_cart)
        super()._wait_until_element_is_visible(self._cart_title, 10)
        return super()._is_displayed(self._cart_title)

    def cart_list_not_empty(self) -> bool:
        super()._wait_until_element_is_visible(self._cart_item, 10)
        return super()._is_displayed(self._cart_item)

    def checkout(self):
        super()._click(self._checkout_button)

    def checkout_title(self) -> bool:
        super()._wait_until_element_is_visible(self._checkout_title, 10)
        return super()._is_displayed(self._checkout_title)

    def execute_checkout(self, firstname: str, lastname: str, postalcode: str):
        super()._type(self._first_name_locator, firstname)
        super()._type(self._last_name_locator, lastname)
        super()._type(self._postal_code_locator, postalcode)
        super()._click(self._continue_button)

    def checkout_overview_text(self):
        return super()._get_text(self._checkout_overview)

    def payment_information(self) -> bool:
        super()._wait_until_element_is_visible(self._payment_information, 10)
        return super()._is_displayed(self._payment_information)

    def finish_purchase(self) -> bool:
        super()._click(self._finish_button)
        super()._wait_until_element_is_visible(self._message_complete_order, 10)
        return super()._is_displayed(self._message_complete_order)



