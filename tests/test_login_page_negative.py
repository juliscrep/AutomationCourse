import pytest
from Page_Objects.login_page import LoginPage


@pytest.mark.loginpagenegativo
class TestNegativeScenarios:
    @pytest.mark.parametrize("username , password , expected_error_message",
                             [("Incorrectuser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_login_negative(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)

        assert login_page.is_displayed(), "Error message is not displayed"

        assert login_page.get_error_message() == expected_error_message, "Your message is not expected"

