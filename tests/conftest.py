import pytest
from src.plc_stub import FakePLC
import logging

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def plc_connection():
    plc = FakePLC()

    try:
        """
        Ensuring PLC is stopped before and after tests
        """
        plc.stop_cycle()
        yield plc
    finally:
        """Tearing Down"""
        try:
            plc.stop_cycle()
        except Exception as e:
            logger.error("Failed to stop PLC during teardown", exc_info=e)
