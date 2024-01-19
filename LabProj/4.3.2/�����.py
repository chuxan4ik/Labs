# Программирование на языке высокого уровня (Python).
# Задание 4.3.1
# Вариант 3
# Выполнил: Воронкова Е.А.
# Группа: ПИН-б-з-22-1
# E-mail: 

import time
from пицца import *


class Заказ:
    """Класс Заказ содержит информацию о заказе."""

    # Переменная класса для определения номера заказа
    счетчик_заказов = 0

    def __init__(self):
        """Конструктор класса."""
        # Хранит экземпляры класса Пицца и его потомков
        self.заказанные_пиццы = []
        Заказ.счетчик_заказов += 1
        self.номер_заказа = Заказ.счетчик_заказов

    def __str__(self):
        """Вернуть содержимое заказа и его сумму.

        Формат вывода:

        Заказ №2
        1. Пицца: Пепперони | Цена: 350.00 р.
           Тесто: тонкое Соус: томатный
           Начинка: пепперони, сыр моцарелла
        2. Пицца: Барбекю | Цена: 450.00 р.
           Тесто: тонкое Соус: барбекю
           Начинка: бекон, ветчина, зелень, сыр моцарелла
        Сумма заказа: 800.00 р.

        """
        res = (
                f'Заказ №{self.номер_заказа}\n' +
                '\n'.join([f'{i + 1}. ' + str(pizza) for i, pizza in enumerate(self.заказанные_пиццы)]))
        return res

    def добавить(self, пицца):
        """Добавить пиццу в заказ."""
        self.заказанные_пиццы.append(пицца)

    def сумма(self):
        """Вернуть сумму заказа."""
        return sum(pizza.цена for pizza in self.заказанные_пиццы)

    def выполнить(self):
        """Выполнить заказ.

        Для каждой пиццы в заказе: подготовить, испечь, нарезать и упаковать.
        Сообщить, что заказ готов и пожелать приятного аппетита.

        Для визуального эффекта, каждое действие осуществляется с "задержкой",
        используя time.sleep(1).

        Формат вывода:

        Заказ поступил на выполнение...
        1. Пепперони
        Начинаю готовить пиццу Пепперони
          - замешиваю тонкое тесто...
          - добавляю соус: томатный...
          - и, конечно: пепперони, сыр моцарелла...
        Выпекаю пиццу... Готово!
        Нарезаю на аппетитные кусочки...
        Упаковываю в фирменную упаковку и готово!

        Заказ №2 готов! Приятного аппетита!
        """
        for i, pizza in enumerate(self.заказанные_пиццы, start=1):
            print(f'{i}. {pizza.название}')
            pizza.подготовить()
            pizza.испечь()
            pizza.нарезать()
            pizza.упаковать()
        print(f'Заказ №{self.номер_заказа} готов! Приятного аппетита!')


