import pytest
from src.system_controller_stub import SystemController


def test_system_starts_and_processes_module(plc_connection):
    """
    Verifies the interaction between PLC + Controller + Vision logic
    """
    system = SystemController(plc_connection)
    
    # Confirming if the system is disconnected as precondition
    assert plc_connection.is_running() is False

    # Starting PLC + controller interaction
    system.start_system()
    assert plc_connection.is_running() is True

    # Assertion: Capture and process a valid frame of the module
    frame = {"modules": 1}
    result = system.capture_and_process_module(frame)
    assert result == "MODULE_PROCESSED"
    
    # Clean up of the PLC state after test is finished
    plc_connection.stop_cycle()


def test_system_handles_no_module_detected(plc_connection):
    """
    Verifies the system behavior when vision detects nothing
    """
    system = SystemController(plc_connection)

    # Starting PLC + controller interaction
    system.start_system()
    assert plc_connection.is_running() is True

    # Assertion: Detects a frame with a missing module
    empty_frame = {"modules": 0}
    result = system.capture_and_process_module(empty_frame)
    assert result == "NO_MODULE"
    
    # Clean up of the PLC state after test is finished
    plc_connection.stop_cycle()


def test_plc_state_is_not_modified_by_failed_detection(plc_connection):
    """
    PLC should remain running even if detection fails, because it's not a system fault
    """
    system = SystemController(plc_connection)
    system.start_system()

    # Assertion: Detects a frame with a missing module, but PLC remains working
    empty_frame = {"modules": 0}
    system.capture_and_process_module(empty_frame)
    assert plc_connection.is_running() is True
    
    # Clean up of the PLC state after test is finished
    plc_connection.stop_cycle()
