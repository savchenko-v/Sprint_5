import random


class Help:  # функции, которые генерируют имя, логин и пароль
    @staticmethod
    def generate_email():
        return f'tester_toster{random.randint(100, 999)}@yandex.ru'

    @staticmethod
    def generate_password():
        return f'{random.randint(100000, 999999)}'
