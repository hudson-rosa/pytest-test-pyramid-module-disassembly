import pytest  # type: ignore
from src.vision_stub import detect_modules_on_belt
from .logger.log_info import show_module_results as show_result


HAPPY_PATH_CASES = [
    pytest.param(1, True, id="one-module"),
    pytest.param(2, True, id="two-modules"),
]

EDGE_CASES = [
    pytest.param(None, True, id="unknown-module"),
    pytest.param(-1, True, id="invalid-reading"),
]


@pytest.mark.parametrize("total_modules, expected", HAPPY_PATH_CASES)
def test_detect_modules_on_conveyor_belt(total_modules, expected):
    frame = {"modules": total_modules}
    detection_result = detect_modules_on_belt(frame)

    show_result(frame, detection_result)
    assert detection_result is expected


def test_no_modules_detected_on_conveyor_belt():
    empty_frame = {"modules": 0}
    detection_result = detect_modules_on_belt(empty_frame)

    show_result(empty_frame, detection_result)
    assert detect_modules_on_belt(empty_frame) is False


@pytest.mark.parametrize("total_modules, expected", EDGE_CASES)
def test_invalid_module_detection(total_modules, expected):
    empty_frame = {"modules": total_modules}
    detection_result = detect_modules_on_belt(empty_frame)

    show_result(empty_frame, detection_result)
    assert detection_result is not expected
