from pytest_bdd import given, when, then, parsers


@given("the operator is on the dashboard page")
def given_the_operator_is_on_the_dashboard_page(dashboard_page):
    dashboard_page._wait_until_status_is_loaded()


@given(parsers.parse('the system status indicator is "{expected_status}"'))
def given_the_system_operator_is_available(dashboard_page, expected_status):
    dashboard_page.get_status_text() == expected_status


@when(parsers.parse('the operator enters module number "{module_number}"'))
def when_the_operator_enters_module_number(dashboard_page, module_number):
    dashboard_page.enter_module_number(module_number)


@then(parsers.parse('the page title should "{expected_title}"'))
def then_the_page_title_is_displayed(dashboard_page, expected_title):
    assert dashboard_page.get_title() == expected_title


@when("clicks the [Check Status] button")
def when_clicks_the_check_status_button(dashboard_page):
    dashboard_page.click_check_status_button()


@then(parsers.parse('the system status indicator shows "{expected_status}"'))
def then_the_status_indicator_shows_the_system_condition(
    dashboard_page, expected_status
):
    assert dashboard_page.get_status_text() == expected_status
    assert dashboard_page.is_status_visible()


@then(parsers.parse('the module status shows "{expected_module_status}"'))
def then_the_module_status_shows_the_expected_text(
    dashboard_page, expected_module_status
):
    assert dashboard_page.get_module_status_text() == expected_module_status
