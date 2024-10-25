class Resource:

    def __init__(self, name:str, resource_type:str):
        self.name = name
        self.resource_type = resource_type
    
    def __del__(self):
        print(f"Ресурс {self.name} типа {self.resource_type} удален.")

r1 = Resource("Соединение1", "подключение к базе данных")
r2 = Resource("Соединение2", "подключение к базе данных")

for _ in range(1, 11):
    print(_)
    if _ == 5:
        del r2