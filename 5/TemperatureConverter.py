class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @classmethod
    def from_kelvin(cls, kelvin):
        celsius = kelvin - 273.15
        return cls(celsius)

    def __init__(self, celsius):
        self.celsius = celsius

    def __str__(self):
        return f"{self.celsius}°C"

# 2
class Employee:
    @staticmethod
    def is_valid_age(age):
        return 18 <= age <= 65

    @classmethod
    def from_string(cls, data_string):
        name, age_str, position = data_string.split(', ')
        age = int(age_str)
        if not cls.is_valid_age(age):
            raise ValueError("Invalid age")
        return cls(name, age, position)

    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def get_details(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Должность: {self.position}"