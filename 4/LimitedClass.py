class LimitedClass:
    _instances = []
    _max_instances = 5

    def __new__(cls, *args, **kwargs):
        if len(cls._instances) < cls._max_instances:
            instance = super().__new__(cls)
            cls._instances.append(instance)
            return instance
        else:
            return cls._instances[-1]

    def __init__(self, value):
        self.value = value

# 2
class Book:
    _unique_books = {}

    def __new__(cls, title, author, year):
        key = (title, author)
        if key in cls._unique_books:
            return cls._unique_books[key]
        else:
            instance = super().__new__(cls)
            cls._unique_books[key] = instance
            return instance
