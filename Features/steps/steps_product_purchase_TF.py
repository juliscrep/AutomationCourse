from behave import given, when, then
from Page_Objects_TF.login_page_TF import LoginPageTF


@given(u'the user successfully logs in using the username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page = LoginPageTF(context.driver)
    context.login_page.open()
    context.login_page.execute_login(username, password)
    assert context.login_page.get_text_header() == "Swag Labs", "Header is not expected"


@when(u'the user selects the product named "{product_name}" to add to the shopping cart')
def step_impl(context, product_name):
    pass


@when(u'goes to the shopping cart and checks out')
def step_impl(context):
    pass


@then(u'the user completes the checkout information using first name "{first_name}", last name "{last_name}" '
      u'and postal code "{postal_code}"')
def step_impl(context, first_name, last_name, postal_code):
    pass


@then(u'finalizes the purchase order')
def step_impl(context):
    pass
