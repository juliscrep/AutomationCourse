from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from Page_Objects_TF.page_base_TF import BasePageTF


class LoginPageTF(BasePageTF):

    __url ="https://www.saucedemo.com/"
    __username_field = (By.ID, "user-name")
    __password_field = (By.ID, "password")
    __login_button = (By.NAME, "login-button")
    _product_title = (By.XPATH, "//SPAN[@class='title'][text()='Products']")
    _product_list = (By.XPATH, "//DIV[@id='inventory_container']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__login_button)

    def product_section_visible(self) -> bool:
        return super()._is_displayed(self._product_title) and super()._is_displayed(self._product_title)

    def get_text_title(self) -> str:
        return super()._get_text(self._product_title)