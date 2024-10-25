import re
from string import digits, ascii_lowercase

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
        return bool(re.match(pattern, number))
    
    @classmethod
    def check_name(cls, name):
        words = name.split()
        if len(words) != 2:
            return False
        
        first_name, last_name = words
        return all(char in cls.CHARS_FOR_NAME for char in first_name) and \
               all(char in cls.CHARS_FOR_NAME for char in last_name)