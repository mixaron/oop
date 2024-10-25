class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)
print(s1)
print(s2)