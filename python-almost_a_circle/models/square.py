"""create a class named Square that inherits from Rectangle """
from models.rectangle import Rectangle

class Square(Rectangle):
    """ define the class Square"""
    def __init__(self, size):
        """ define the class Square"""
        self.__width = 0
        self.__height = 0
        self.__size = size

    @property
    def size(self):
        """ define the class Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """ define the class Square"""
        if value <= 0:
            raise ValueError("Size must be a positive number.")
        self.__width = value
        self.__height = value
        self.__size = value

    def get_area(self):
        """ define the class Square"""
        return self.__width * self.__height