import pytest

from selenium import webdriver


# from utils import attach

@pytest.fixture(scope='function')
def setup_browser(request):



    capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVideo": True
        }
    }

    driver = webdriver.Remote(
        command_executor="https://selenoid.autotests.cloud/wd/hub",
        desired_capabilities=capabilities)

    driver.maximize_window()

    yield browser
    browser.quit()