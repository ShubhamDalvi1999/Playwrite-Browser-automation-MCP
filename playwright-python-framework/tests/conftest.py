import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def pytest_addoption(parser):
    parser.addoption("--browser-name", action="store", default="chromium")

@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('--browser-name') or 'chromium'
    with sync_playwright() as playwright:
        if browser_name == 'chromium':
            browser = playwright.chromium.launch(headless=False)
        elif browser_name == 'firefox':
            browser = playwright.firefox.launch(headless=False)
        elif browser_name == 'webkit':
            browser = playwright.webkit.launch(headless=False)
        else:
            raise ValueError(f'Unsupported browser: {browser_name}')
        yield browser
        browser.close()

@pytest.fixture(scope='function')
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope='function')
def login_page(page):
    return LoginPage(page) 