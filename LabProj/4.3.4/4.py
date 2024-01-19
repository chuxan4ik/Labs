# Программирование на языке высокого уровня (Python).
# Задание 4.3.1
# Вариант 3
# Выполнил: Воронкова Е.А.
# Группа: ПИН-б-з-22-1
# E-mail: 
import json
# Создаём класс Money
class Money:
    # Специальные методы
    def __init__(self, value=0):
        # Инициализируем поле-данные
        self.value = value
    def __int__(self, *args, **kwargs):
        # Инициализация класса с параметрами
        if args and isinstance(args[0], (int, float)):
            self.value = args[0]
        elif args:
            self.value = int(args[0])
        elif kwargs:
            self.value = int(kwargs['value'])
    def __str__(self):
        # Возвращаем строковое представление объекта
        return str(self.value)
    def __add__(self, other):
        # Сложение двух объектов класса Money
        return Money(self.value + other.value)
    def __sub__(self, other):
        # Вычитание двух объектов класса Money
        return Money(self.value - other.value)
    def __mul__(self, other):
        # Умножение двух объектов класса Money
        return Money(self.value * other.value)
    def __truediv__(self, other):
        # Деление двух объектов класса Money
        return Money(self.value / other.value)
    def save(self, filename='money.json'):
        # Сохраняем объект в JSON-файл filename
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.value, f)
    def load(self, filename='money.json'):
        # Загружаем объект из JSON-файл filename
        with open(filename, 'r', encoding='utf-8') as f:
            self.value = json.load(f)
# Создаём класс Money
class Money:
    # Специальные методы
    def __init__(self, value=0):
        # Инициализируем поле-данные
        self.value = value
    def __int__(self, *args, **kwargs):
        # Инициализация класса с параметрами
        if args and isinstance(args[0], (int, float)):
            self.value = args[0]
        elif args:
            self.value = int(args[0])
        elif kwargs:
            self.value = int(kwargs['value'])
    def __str__(self):
        # Возвращаем строковое представление объекта
        return str(self.value)
    def __add__(self, other):
        # Сложение двух объектов класса Money
        return Money(self.value + other.value)
    def __sub__(self, other):
        # Вычитание двух объектов класса Money
        return Money(self.value - other.value)
    def __mul__(self, other):
        # Умножение двух объектов класса Money
        return Money(self.value * other.value)
    def __truediv__(self, other):
        # Деление двух объектов класса Money
        return Money(self.value / other.value)
    def save(self, filename='money.json'):
        # Сохраняем объект в JSON-файл filename
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.value, f)
    def load(self, filename='money.json'):
        # Загружаем объект из JSON-файл filename
        with open(filename, 'r', encoding='utf-8') as f:
            self.value = json.load(f)
# Создаём объект класса Money
obj_money = Money(10)
# Сохраняем объект в файл
obj_money.save()
# Загружаем объект из файла
obj_money.load()
