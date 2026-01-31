import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

# from utils import attach

@pytest.fixtrue(scope='function')
def setup_browser(request):

    options = Options()
    capabilselenoid_capabilitieities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilitie)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        desired_capabilities=capabilities)

    browser = Browser(Config(driver))
    yield browser

    browser.quit()