from src.plc_stub import FakePLC
from .logger.log_info import show_plc_results as show_results


def test_plc_starts_cycle(plc_connection):
    plc_connection.start_cycle()
    assert plc_connection.is_running() is True


def test_plc_stops_cycle(plc_connection):
    plc_connection.stop_cycle()
    assert plc_connection.is_running() is False
