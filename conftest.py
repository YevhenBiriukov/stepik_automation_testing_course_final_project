import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})
    browser = None
    if browser_name == "chrome":
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
