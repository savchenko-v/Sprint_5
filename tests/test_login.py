from data import Data
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:

    # вход по кнопке «Войти в аккаунт» на главной
    def test_login_main_page(self, driver):
        enter_button = driver.find_element(*Locators.ENTER_BUTTON_MAIN_PAGE)
        enter_button.click()

        email_input = driver.find_element(*Locators.EMAIL_INPUT_FIELD)
        email_input.send_keys(Data.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.PASSWORD_INPUT_FIELD)
        password_input.send_keys(Data.AUTH_PASSWORD)

        submit_button = driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON)
        submit_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

        order_button = driver.find_element(*Locators.ORDER_BUTTON)
        # при успешном входе отображается главная страница и есть кнопка "Оформить заказ"
        assert driver.current_url == Data.BURGERS_MAIN_URL and order_button.text == 'Оформить заказ'

    # вход через кнопку «Личный кабинет»
    def test_login_personal_account(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(Data.AUTH_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(Data.AUTH_PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

        order_button = driver.find_element(*Locators.ORDER_BUTTON)
        assert driver.current_url == Data.BURGERS_MAIN_URL and order_button.text == 'Оформить заказ'

    # вход через кнопку в форме регистрации
    def test_login_register_page(self, driver):
        driver.get(Data.REGISTER_URL)

        driver.find_element(*Locators.ENTER_BUTTON_LOGIN_PAGE).click()
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(Data.AUTH_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(Data.AUTH_PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

        order_button = driver.find_element(*Locators.ORDER_BUTTON)
        assert driver.current_url == Data.BURGERS_MAIN_URL and order_button.text == 'Оформить заказ'

    # вход через кнопку в форме восстановления пароля
    def test_login_forgot_password_page(self, driver):
        driver.get(Data.FORGOT_PASSWORD_PAGE_URL)

        driver.find_element(*Locators.ENTER_BUTTON_LOGIN_PAGE).click()
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(Data.AUTH_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(Data.AUTH_PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

        order_button = driver.find_element(*Locators.ORDER_BUTTON)
        assert driver.current_url == Data.BURGERS_MAIN_URL and order_button.text == 'Оформить заказ'
