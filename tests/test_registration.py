from data import Data
from locators import Locators
from helpers import Help
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration:

    # проверка успешной регистрации, использованы функции генерации логина и пароля
    def test_registration_valid_values(self, driver):
        driver.get(Data.REGISTER_URL)

        driver.find_element(*Locators.NAME_INPUT_FIELD_REG).send_keys('toster')
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_REG).send_keys(Help.generate_email())
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD_REG).send_keys(Help.generate_password())
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON))

        # при успешной регистрации отображается страница входа
        assert driver.current_url == Data.LOGIN_URL

    # нельзя зарегистрироваться с пустым полем Имя
    def test_registration_empty_name(self, driver):
        driver.get(Data.REGISTER_URL)

        driver.find_element(*Locators.EMAIL_INPUT_FIELD_REG).send_keys(Help.generate_email())
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD_REG).send_keys(Help.generate_password())
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        assert driver.current_url == Data.REGISTER_URL  # остаёмся на странице регистрации

    # проверка ошибки для некорректного пароля
    def test_registration_invalid_password(self, driver):
        driver.get(Data.REGISTER_URL)

        driver.find_element(*Locators.NAME_INPUT_FIELD_REG).send_keys('toster')
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_REG).send_keys(Help.generate_email())
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD_REG).send_keys('123')
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        invalid_password_error = driver.find_element(*Locators.INVALID_PASSWORD_ERROR)
        assert invalid_password_error.text == 'Некорректный пароль'
