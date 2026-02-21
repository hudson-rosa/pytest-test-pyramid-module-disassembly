from pytest_bdd import given, when, then
from src.system_controller_stub import SystemController


@given("the system is ready", target_fixture="system")
def given_the_system_is_ready(plc_connection):
    plc_connection.stop_cycle()
    assert plc_connection.is_running() is False
    return SystemController(plc_connection)


@when("a cycle is started")
def when_a_cycle_is_started(system):
    system.start_system()


@when("an image is captured with a module", target_fixture="capture_result")
def when_an_image_is_captured_with_a_module(system):
    frame = {"modules": 1}
    return system.capture_and_process_module(frame)


@then("the module is processed successfully")
def then_the_module_is_processed(capture_result, plc_connection):
    assert plc_connection.is_running() is True
    assert capture_result == "MODULE_PROCESSED"
