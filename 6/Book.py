class Book:
    
    def __init__(self, title, author, pages):
        self.title = title
        self._author = author
        self.__pages = pages
    
    def get_author(self):
        return self._author
    
    def set_author(self, author):
        self._author = author

    def get_pages(self):
        return self.__pages
    
    def set_pages(self, pages):
        if pages > 0:
            self.__pages = pages
        else:
            raise ValueError("Кол-во страниц должно быть положительным числом.")
        
    def display_info(self):
        return f"Название: '{self.title}', Автор: {self._author} Страниц: {self.__pages}"