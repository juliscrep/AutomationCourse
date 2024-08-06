from behave import given, when, then
from Page_Objects_TF.login_page_TF import LoginPageTF
from Page_Objects_TF.product_purchase_TF import ProductPageTF


@given(u'the user successfully logs in using the username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page = LoginPageTF(context.driver)
    context.login_page.open()
    context.login_page.execute_login(username, password)
    assert context.login_page.get_text_title() == "Products", "Title is not expected"
    assert context.login_page.product_section_visible(), "Product section should be visible"


@when(u'the user selects the product to add to the shopping cart')
def step_impl(context):
    context.product_page = ProductPageTF(context.driver)
    assert context.product_page.product_displayed(), "The product should be displayed"
    context.product_page.select_product()


@when(u'goes to the shopping cart and checks out')
def step_impl(context):
    context.product_page.go_to_shopping_cart()
    assert context.product_page.cart_list_not_empty(), "The cart list should not be empty"
    context.product_page.checkout()
    assert context.product_page.checkout_title(), "The checkout title should be visible"


@then(u'the user completes the checkout information using first name "{firstname}", last name "{lastname}" '
      u'and postal code "{postalcode}"')
def step_impl(context, firstname, lastname, postalcode):
    context.product_page.execute_checkout(firstname, lastname, postalcode)


@then(u'finalizes the purchase order')
def step_impl(context):
    assert context.product_page.cart_list_not_empty(), "The cart list should not be empty"
    assert context.product_page.checkout_overview_text() == "Checkout: Overview", "Title is not expected"
    assert context.product_page.payment_information(), "The payment information should be visible"
    assert context.product_page.finish_purchase(), ("The message confirming your order completion"
                                                    " should be visible")

