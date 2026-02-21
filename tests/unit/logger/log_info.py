import logging

logger = logging.getLogger(__name__)


def show_module_results(frame, detection_result):
    logger.info("--> Total modules with frame = %s", frame)
    logger.info("--> Module(s) in the belt - Result = %s", detection_result)
    
def show_plc_results(action, plc_state):
    logger.info("--> PLC action performed: %s", action)
    logger.info("--> PLC current state: %s", plc_state)
