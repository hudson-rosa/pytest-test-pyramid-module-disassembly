import logging

logger = logging.getLogger(__name__)

class FakePLC:
    def __init__(self):
        self.started = False

    def start_cycle(self):
        logger.info("PLC cycle started")
        self.started = True

    def stop_cycle(self):
        logger.info("PLC cycle stopped / disconnected")
        self.started = False

    def is_running(self):
        logger.info("PLC is running")
        return self.started
