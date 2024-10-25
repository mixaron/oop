class Employee:
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 30000:
            raise ValueError("Зарплата должна быть не менее 30000")
        self._salary = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @age.deleter
    def age(self):
        self._age = None

    def apply_raise(self, percentage):
        if percentage < 0:
            raise ValueError("Процент повышения должен быть положительным")
        self.salary *= (1 + percentage / 100)