def introspection_info(obj):
    # Определяем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты и методы
    attributes_and_methods = dir(obj)

    # Получаем модуль (с обработкой отсутствия атрибута)
    obj_module = getattr(obj, '__module__', None)

    # Разделяем атрибуты и методы
    attributes = [item for item in attributes_and_methods if
                  not callable(getattr(obj, item)) and not item.startswith("__")]
    methods = [item for item in attributes_and_methods if callable(getattr(obj, item)) and not item.startswith("__")]

    # Создаем словарь с информацией
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
    }

    return info


# Пример использования
number_info = introspection_info(42)
print(number_info)


# Пример использования с пользовательским классом
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"


my_object = MyClass("Alice")
class_info = introspection_info(my_object)
print(class_info)
