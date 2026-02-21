def detect_modules_on_belt(captured_module_frame):
    """
    This is a fake vision logic: image is a list of pixels where 1 = module, 0 = belt (background)
    """
    modules = captured_module_frame.get("modules")
    return modules is not None and modules >= 1
