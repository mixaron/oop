class Car:
    
    def __init__(self, model, year, mileage):
        self.model = model
        self._year = year
        self.__mileage = mileage

    def get_year(self):
        return self._year
    
    def set_year(self, year): 
        if year < 1886 or year > 2024:
            raise ValueError("Год не может быть меньше чем 1886 и больше чем 2024")
        self._year = year
    
    def get_mileage(self):
        return self.__mileage
    
    def set_mileage(self, mileage):
        if mileage < 0:
            raise ValueError("Пробег не может быть отрицательным")
        self.__mileage = mileage