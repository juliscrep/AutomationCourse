from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from Page_Objects.page_base import BasePage


class LoggedInSuccessfullyPage(BasePage):

    _url = "https://practicetestautomation.com/logged-in-successfully/"
    _header_locator= (By.TAG_NAME, "h1")
    _logout_locator= (By.XPATH, "//A[@class='wp-block-button__link has-text-color has-background has-very-dark-gray-background-color'][text()='Log out']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self._url

    def header(self) -> str:
        return super()._get_text(self._header_locator)

    def logout_button_displayed(self) -> bool:
        return super()._is_displayed(self._logout_locator)

