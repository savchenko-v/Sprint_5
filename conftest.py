import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.get(Data.BURGERS_MAIN_URL)
    WebDriverWait(chrome_driver, 3)

    yield chrome_driver

    chrome_driver.quit()


@pytest.fixture
def login(driver):
    driver.get(Data.LOGIN_URL)

    driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(Data.AUTH_EMAIL)
    driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(Data.AUTH_PASSWORD)
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.ORDER_BUTTON))
    return driver
