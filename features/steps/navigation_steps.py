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
