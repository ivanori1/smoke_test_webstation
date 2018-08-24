from behave import step


@step('Open WebStation login page')
def step_impl(context):
    context.selenium_driver.navigate("http://webstationtest3.ttweb.net/WebStation.aspx")


@step('Click on Login button')
def step_impl(context):
    context.login_page.click_login_button()


@step('Error appears: "{error}"')
def step_impl(context, error):
    context.login_page.verify_failed_login(error)
