from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    STATUS_INDICATOR_LABEL = (By.ID, "system-status")
    MODULE_NUMBER_INPUT = (By.ID, "module-number")
    CHECK_STATUS_BUTTON = (By.ID, "check-status-button")
    MODULE_STATUS_LABEL = (By.ID, "module-status")

    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str):
        self.driver.get(url)

    def _wait_until_status_is_loaded(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.STATUS_INDICATOR_LABEL)
        )

    def get_title(self) -> str:
        return self.driver.title

    def get_status_text(self) -> str:
        status_element = self.driver.find_element(*self.STATUS_INDICATOR_LABEL)
        return status_element.text

    def is_status_visible(self) -> bool:
        is_status_element_displayed = self.driver.find_element(
            *self.STATUS_INDICATOR_LABEL
        ).is_displayed()
        return is_status_element_displayed

    def enter_module_number(self, module_number: str):
        module_input = self.driver.find_element(*self.MODULE_NUMBER_INPUT)
        module_input.clear()
        module_input.send_keys(module_number)

    def click_check_status_button(self):
        status_button = self.driver.find_element(*self.CHECK_STATUS_BUTTON)
        status_button.click()

    def get_module_status_text(self) -> str:
        module_status_element = self.driver.find_element(*self.MODULE_STATUS_LABEL)
        return module_status_element.text
