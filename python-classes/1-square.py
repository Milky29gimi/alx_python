
""" create a class called square
and define a private instance attribute calles size. 
Size validation- input validater"""

class Square:
    __size= ()
    def __init__(self, size=0):
    """ create a class called square
and define a private instance attribute calles size. 
Size validation- input validater"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
