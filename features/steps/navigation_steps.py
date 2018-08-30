from behave import step, then


@step('Navigation Box is visible')
def step_impl(context):
    assert context.header_page.navigation_box_is_visible()


@step('Click on News Button')
def step_impl(context):
    context.header_page.click_news_navigation()


@step('Click on customize and control button')
def step_impl(context):
    context.header_page.click_on_costomize_and_control()


@step('Click on Set As Start Page')
def step_impl(context):
    context.header_page.click_on_set_as_start_page()


@step('Click on Home button')
def step_impl(context):
    context.header_page.click_on_home_button()


@then('News detail page will appear')
def step_impl(context):
    assert context.header_page.is_news_header_visible()
