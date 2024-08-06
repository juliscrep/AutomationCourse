from behave import given, when, then
from Page_Objects_TF.login_page_TF import LoginPageTF
import allure


@given(u'the user is on the login page')
def step_impl(context):
    context.login_page = LoginPageTF(context.driver)
    context.login_page.open()


@when('the user types the username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.execute_login(username, password)


@then(u'shows home page')
def step_impl(context):
    assert context.login_page.get_text_title() == "Products", "Title is not expected"
    assert context.login_page.product_section_visible(), "Product section should be visible"



