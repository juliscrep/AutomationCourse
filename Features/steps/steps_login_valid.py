from behave import given, when, then

from Page_Objects.logged_in_successfully import LoggedInSuccessfullyPage
from Page_Objects.login_page import LoginPage
import allure


@given(u'I open a new page')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()


@when('I enter a valid username "{user}" and password "{password}"')
def step_impl(context, user, password):
    context.login_page.execute_login(user, password)


@then('I should see the message "{results}"')
def step_impl(context, results):
    context.logged_in_page = LoggedInSuccessfullyPage(context.driver)
    assert context.logged_in_page.expected_url == context.logged_in_page.current_url(), ("Actual URL is not the same "
                                                                                         "as expected")
    assert context.logged_in_page.header() == results, "Header is not expected"
    assert context.logged_in_page.logout_button_displayed(), "Logout button should be displayed"
