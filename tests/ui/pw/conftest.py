import pytest
from playwright.sync_api import sync_playwright
from tests.ui.common.base_page import BasePage
from tests.ui.pw.pages.dashboard_page import DashboardPage

pytest_plugins = [
    "tests.ui.pw.steps.calangobotics_dashboard_steps",
]


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(
        headless=False, args=["--no-sandbox", "--disable-dev-shm-usage"]
    )
    yield browser
    browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def dashboard_page(page):
    dashboard = DashboardPage(page)
    dashboard.open(BasePage.get_dashboard_path().as_uri())
    return dashboard
