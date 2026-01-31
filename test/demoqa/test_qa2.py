
from selene import browser, be, have, by
from selenium.webdriver import Keys

firstName = 'Иван'
lastName = 'Иванов'
mail = 'random@mail.ru'
number = '8800123456'
date = '01 Jan 2026'
addres = 'Россия, г. Мытищи, Ленинская ул., д. 16 кв.194'
state = 'Haryana'
city = 'Karnal'

def test_form_ru():

    browser.open('/')

    # Ввод первого имени
    browser.element('#firstName').should(be.blank).type(firstName)

    # ввод второго имени
    browser.element('#lastName').should(be.blank).type(lastName)

    # ввод почты
    browser.element('#userEmail').should(be.blank).type(mail)

    # Нажатие кнопки (перекрыто label, нажатие через него)
    browser.element('[for="gender-radio-1"]').click()

    # ввод номера
    browser.element('#userNumber').type(number)

    # ввод даты вручную
    browser.element('#dateOfBirthInput').send_keys(
        Keys.CONTROL + 'a',
        Keys.NULL,
        '01.01.2020',
        Keys.ENTER,
    )

    # проверка сохранения даты
    browser.element('#dateOfBirthInput').should(have.value('01 Jan 2020'))

    # ввод адреса
    browser.element('#currentAddress').type(addres)

    # выбор штата
    browser.all('[class=" css-1wy0on6"]').first.click()
    browser.element(by.text(state)).click()

    # выбор города
    browser.all('[class=" css-1wy0on6"]').second.click()
    browser.element(by.text(city)).click()

    # # подтверждения
    browser.element('#submit').click()

    # проверка заполнености
    browser.element('[class="modal-content"').should(be.visible)
    browser.element('[class="table-responsive"]').should(have.text(f'{firstName} {lastName}'))
    browser.element('[class="table-responsive"]').should(have.text(mail))
    browser.element('[class="table-responsive"]').should(have.text(number))
    browser.element('[class="table-responsive"]').should(have.text(addres))
    browser.element('[class="table-responsive"]').should(have.text(state + ' ' + city))

