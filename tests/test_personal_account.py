from data import UrlData
from data import TimeData
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPersonalAccount:

    # переход по клику на «Личный кабинет»
    def test_move_to_personal_account(self, driver, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, TimeData.WAIT_TIME).until(EC.visibility_of_element_located(Locators.EXIT_BUTTON))

        exit_button = driver.find_element(*Locators.EXIT_BUTTON)
        assert driver.current_url == UrlData.PROFILE_URL and exit_button.is_displayed()

    # переход по клику на «Конструктор»
    def test_click_to_constructor(self, driver, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        collect_burger_title = driver.find_element(*Locators.COLLECT_BURGER_TITLE)
        assert driver.current_url == UrlData.BURGERS_MAIN_URL and collect_burger_title.is_displayed()

    # переход по клику на логотип Stellar Burgers
    def test_click_to_logo_burgers(self, driver, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        driver.find_element(*Locators.LOGO_LOCATOR).click()
        collect_burger_title = driver.find_element(*Locators.COLLECT_BURGER_TITLE)
        assert driver.current_url == UrlData.BURGERS_MAIN_URL and collect_burger_title.is_displayed()

    # выход по кнопке «Выход» в личном кабинете
    def test_personal_account_exit(self, driver, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, TimeData.WAIT_TIME).until(EC.visibility_of_element_located(Locators.EXIT_BUTTON))

        driver.find_element(*Locators.EXIT_BUTTON).click()
        WebDriverWait(driver, TimeData.WAIT_TIME).until(EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON))
        assert driver.current_url == UrlData.LOGIN_URL
