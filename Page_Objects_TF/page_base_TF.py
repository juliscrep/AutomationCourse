import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.remote import webdriver, webelement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePageTF:

    def __init__(self, driver: webdriver):
        self._driver = driver

    def _find(self, locator: tuple) -> webelement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple):
        self._find(locator).click()

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 30):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _open_url(self, url: str):
        self._driver.get(url)
        self._driver.maximize_window()

    def _get_text(self, locator: tuple) -> str:
        return self._find(locator).text

