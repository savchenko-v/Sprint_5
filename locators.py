from selenium.webdriver.common.by import By


class Locators:
    ENTER_BUTTON_MAIN_PAGE = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт" на главной

    EMAIL_INPUT_FIELD = (By.XPATH, ".//input[@name = 'name']")  # поля ввода email
    PASSWORD_INPUT_FIELD = (By.XPATH, ".//input[@name='Пароль']")  # поле ввода пароля
    LOGIN_SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # кнопка "Войти" в форме входа

    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")

    PERSONAL_ACCOUNT = (By.XPATH, ".//p[text()='Личный Кабинет']")  # кнопка "Личный Кабинет"
    ENTER_BUTTON_LOGIN_PAGE = (By.CLASS_NAME, "Auth_link__1fOlj")  # кнопка "Войти" под формой регистрации

    NAME_INPUT_FIELD_REG = (By.XPATH, ".//label[text() = 'Имя']/following-sibling::input")  # поле ввода имена для регистрации
    EMAIL_INPUT_FIELD_REG = (By.XPATH, ".//label[text() = 'Email']/following-sibling::input")  # поле ввода email для регистрации
    PASSWORD_INPUT_FIELD_REG = (By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input")  # поле ввода пароля для регистрации
    REGISTRATION_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # кнопка "Зарегистрироваться"
    INVALID_PASSWORD_ERROR = (By.XPATH, ".//p[text()='Некорректный пароль']")  # надпись "Некорректный пароль"

    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text() = 'Конструктор']")  # кнопка "Конструктор"
    LOGO_LOCATOR = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")  # лого Stellar Burgers
    COLLECT_BURGER_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']")  # заголовок "Соберите бургер"
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # кнопка "Выход" в личном кабинете

    BREAD_BUTTON = (By.XPATH, ".//span[text()='Булки']")  # кнопка "Булки"
    SAUCES_BUTTON = (By.XPATH, ".//span[text()='Соусы']")  # кнопка "Соусы"
    TOPPINGS_BUTTON = (By.XPATH, ".//span[text()='Начинки']")  # кнопка "Начинки"
    CURRENT_TAB = (By.XPATH, ".//div[contains(@class, 'current')]")  # текущая вкладка из трех: Булки, Соусы, Начинки

