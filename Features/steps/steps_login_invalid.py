from behave import given, when, then
from Page_Objects.login_page import LoginPage
import allure


@given(u'I open the page')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()


@when('I enter username "{user}" and password "{password}"')
def step_impl(context, user, password):
    context.login_page.execute_login(user, password)


@then('I should see the page "{results}"')
def step_impl(context, results):
    assert context.login_page.is_displayed(), "Error message is not displayed"

    assert context.login_page.get_error_message() == results, "Your message is not expected"

