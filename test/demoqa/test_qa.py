import allure
from selene import browser, by, be
from selenium.webdriver import Keys


# Чистый Selene (без шагов)
def test_github_only_selene():

    browser.open('https://github.com/')

    browser.element(('.header-search-button')).click()

    browser.element('[name="query-builder-test"]').send_keys('eroshenkoam/allure-example')
    browser.element('[name="query-builder-test"]').submit()
    # browser.element('[name="query-builder-test"]').send_keys((Keys.ENTER))

    browser.element(by.link_text('eroshenkoam/allure-example')).click()

    browser.element('[data-content="Pull requests"]').click()

    browser.element(by.partial_text('#91')).should(be.visible)

