import logging

from src.vision_stub import detect_modules_on_belt

logger = logging.getLogger(__name__)

class SystemController:
    def __init__(self, plc):
        self.plc = plc

    def start_system(self):
        self.plc.start_cycle()

    def capture_and_process_module(self, frame):
        logger.info("Capturing image from the module")
        has_module = detect_modules_on_belt(frame)

        if not has_module:
            logger.warning("No module detected")
            return "NO_MODULE"

        logger.info("Module detected and processed")
        return "MODULE_PROCESSED"
