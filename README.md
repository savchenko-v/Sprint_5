# Sprint_5 - UI тестирование
#### Автотесты для сервиса Stellar Burgers. Это космический фастфуд: можно собрать и заказать бургер из необычных ингредиентов.

### Реализованные проверки:
1. Регистрация
- Проверка успешной регистрации, использованы функции генерации логина и пароля
- Нельзя зарегистрироваться с пустым полем Имя
- Ошибка для некорректного пароля (пароль должен содержать минимум 6 символов)

2. Вход
- Вход по кнопке «Войти в аккаунт» на главной
- Вход через кнопку «Личный кабинет»
- Вход через кнопку в форме регистрации
- Вход через кнопку в форме восстановления пароля


3. Личный кабинет 
- Переход по клику на «Личный кабинет»
- Переход из личного кабинета в конструктор по клику на «Конструктор»
- Переход из личного кабинета в конструктор по клику на логотип Stellar Burgers
- Выход по кнопке «Выход» в личном кабинете

4. Раздел «Конструктор»
- Переход к разделу «Соусы»
- Переход к разделу «Булки»
- Переход к разделу «Начинки»


> Функции генерации логина и пароля находятся в файле **helpers.py**
