import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tests.ui.common.base_page import BasePage
from tests.ui.se.pages.dashboard_page import DashboardPage

pytest_plugins = [
    "tests.ui.se.steps.calangobotics_dashboard_steps",
]


@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    """Set up Chrome WebDriver using webdriver-manager"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    # driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()


@pytest.fixture
def dashboard_page(browser):
    page = DashboardPage(browser)
    page.open(BasePage.get_dashboard_path().as_uri())
    return page
