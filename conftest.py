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
        command_executor="https://selenoid.autotests.cloud/#/sessions/f534fae9e7a68620b8e1347b78472051",
        desired_capabilities=capabilities)

    driver.maximize_window()

    yield browser
    browser.quit()