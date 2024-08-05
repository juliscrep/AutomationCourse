import pytest
from Page_Objects.login_page import LoginPage
from Page_Objects.logged_in_successfully import LoggedInSuccessfullyPage


class TestPositiveScenarios:

    @pytest.mark.loginpage
    def test_login_positive(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("student", "Password123")
        logged_in_page = LoggedInSuccessfullyPage(driver)
        assert logged_in_page.expected_url == logged_in_page.current_url(), "Actual URL is not the same as expected"
        assert logged_in_page.header() == "Logged In Successfully", "Header is not expected"
        assert logged_in_page.logout_button_displayed(), "Logout button should be displayed"
