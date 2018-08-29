from behave import step, then


@step('Navigation Box is visible')
def step_impl(context):
    context.header_page.navigation_box_is_visible()
