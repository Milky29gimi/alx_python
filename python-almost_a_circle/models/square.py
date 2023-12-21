"""create a class named Square that inherits from Rectangle """
class Square:
    """ define the class Square"""
    def __init__(self, size):
        self.__width = 0
        self.__height = 0
        self.__size = size
""" define the class Square"""
    @property
    def size(self):
        return self.__size
""" define the class Square"""
    @size.setter
    """ define the class Square"""
    def size(self, value)
    """ define the class Square"""
        if value <= 0:
            raise ValueError("Size must be a positive number.")
        self.__width = value
        self.__height = value
        self.__size = value
""" define the class Square"""
    def get_area(self):
        return self.__width * self.__height