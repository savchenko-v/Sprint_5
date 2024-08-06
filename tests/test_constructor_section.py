from locators import Locators


class TestConstructorSection:

    # переход к разделу «Соусы»
    def test_move_to_sauces_tab(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click()

        current_tab = driver.find_element(*Locators.CURRENT_TAB)
        assert current_tab.text == 'Соусы'

    # переход к разделу «Булки»
    def test_move_to_bread_tab(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        driver.find_element(*Locators.BREAD_BUTTON).click()

        current_tab = driver.find_element(*Locators.CURRENT_TAB)
        assert current_tab.text == 'Булки'

    # переход к разделу «Начинки»
    def test_move_to_topping_tab(self, driver):
        driver.find_element(*Locators.TOPPINGS_BUTTON).click()

        current_tab = driver.find_element(*Locators.CURRENT_TAB)
        assert current_tab.text == 'Начинки'
