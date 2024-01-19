# Программирование на языке высокого уровня (Python).
# Задание 4.3.1
# Вариант 3
# Выполнил: Воронкова Е.А.
# Группа: ПИН-б-з-22-1
# E-mail: 

# Импортируем модуль json
import json


# Создаём класс VectorCollection
class VectorCollection:
    # Специальные методы
    def __init__(self):
        # Инициализируем поле-данные
        self.data = []

    #Фун-ция добавления данных в вектор
    def add(self, value):
        self.data.append(value)
    #Фун-ция удаления данных из вектора по индексу
    def remove(self, index):
        del self.data[index]

    #Приведение вектора в понятные для библиотеки json вид
    def formateVector(self):
        result = []
        for i in self.data:
            print('Item ', i)
            result.append({'x': i.x, 'y': i.y})
        return result

    #Сохранение вектора в файл
    def save(self, filename='vectors.json'):
        formattedData = self.formateVector()

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(formattedData, f)

    #Чтение файла
    def load(self, filename='vectors.json'):
        with open(filename, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

# Создаём класс Vector
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


obj_vector_collection = VectorCollection()
obj_vector_1 = Vector(1, 2)
obj_vector_2 = Vector(3, 4)
obj_vector_3 = Vector(5, 6)
obj_vector_collection.add(obj_vector_1)
obj_vector_collection.add(obj_vector_2)
obj_vector_collection.add(obj_vector_3)
obj_vector_collection.save()
obj_vector_collection.load()