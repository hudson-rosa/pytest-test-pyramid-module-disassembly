
class DashboardPage:
    def __init__(self, page):
        self.page = page

        # Locators
        self.status_indicator = page.locator("#system-status")
        self.module_input = page.locator("#module-number")
        self.check_status_button = page.locator("#check-status-button")
        self.module_status = page.locator("#module-status")

    def open(self, url: str):
        self.page.goto(url)

    def wait_until_loaded(self):
        self.status_indicator.wait_for(state="visible")

    def get_title(self) -> str:
        return self.page.title()

    def get_status_text(self) -> str:
        return self.status_indicator.text_content()

    def is_status_visible(self) -> bool:
        return self.status_indicator.is_visible()

    def enter_module_number(self, module_number: str):
        self.module_input.fill(module_number)

    def click_check_status_button(self):
        self.check_status_button.click()

    def get_module_status_text(self) -> str:
        return self.module_status.text_content()
