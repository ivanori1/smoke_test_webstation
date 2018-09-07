from behave import step, then


@step('Open WebStation login page')
def step_impl(context):
    context.selenium_driver.navigate("http://webstationtest3.ttweb.net/WebStation.aspx")


@step('Open WebStation login page with timeout')
def step_impl(context):
    context.selenium_driver.navigate("http://webstationtest3.ttweb.net/WebStation.aspx?timeout=5000")


@step('Select language "{language}"')
def step_impl(context, language):
    context.login_page.select_language(language)


@step('Click on Login button')
def step_impl(context):
    context.login_page.click_login_button()


@then('Error appears: "{error}"')
def step_impl(context, error):
    assert context.login_page.verify_failed_login(error)


@step('Username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.type_username_placeholder(username)
    context.login_page.type_password_placeholder(password)


@step('Stay logged in option is "{status}"')
def step_impl(context, status):
    context.login_page.check_autologin(status)


@step('Accept EULA is "{status}"')
def step_impl(context, status):
    context.login_page.check_eula(status)


@then('A "{button}" button will appear')
def step_impl(context, button):
    if button == "Home":
        assert context.login_page.verify_home_button_visible()
    elif button == "Login":
        assert context.login_page.verify_login_button_visible()


@step('Click on Next button')
def step_impl(context):
    context.login_page.click_on_relog_button()


@then('A "{page}" page will appear')
def step_impl(context, page):
    if page == "Login":
        assert context.login_page.verify_login_button_visible()
    if page == "Home":
        assert context.login_page.verify_home_button_visible()
        context.execute_steps(u"""
        then Logout
        """)
