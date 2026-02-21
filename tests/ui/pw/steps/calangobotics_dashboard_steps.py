from pytest_bdd import given, when, then, parsers


@given("the operator is on the dashboard page")
def given_operator_on_dashboard(dashboard_page):
    dashboard_page.wait_until_loaded()


@given(parsers.parse('the system status indicator is "{expected_status}"'))
def given_system_status_is(dashboard_page, expected_status):
    assert dashboard_page.get_status_text() == expected_status


@when(parsers.parse('the operator enters module number "{module_number}"'))
def when_operator_enters_module_number(dashboard_page, module_number):
    dashboard_page.enter_module_number(module_number)


@when("clicks the [Check Status] button")
def when_clicks_check_status(dashboard_page):
    dashboard_page.click_check_status_button()


@then(parsers.parse('the page title should "{expected_title}"'))
def then_page_title_should_be(dashboard_page, expected_title):
    assert dashboard_page.get_title() == expected_title


@then(parsers.parse('the system status indicator shows "{expected_status}"'))
def then_system_status_shows(dashboard_page, expected_status):
    assert dashboard_page.get_status_text() == expected_status
    assert dashboard_page.is_status_visible()


@then(parsers.parse('the module status shows "{expected_module_status}"'))
def then_module_status_is(dashboard_page, expected_module_status):
    assert dashboard_page.get_module_status_text() == expected_module_status