"""create a class named Square that inherits from Rectangle """
class Square:
    """ define the class Square"""

    def __init__(self, size):
        self.__width = 0
        self.__height = 0
        self.__size = size

""" Call the super class with id, x, y, width and height 
- this super call will use the logic of the __init__ of 
the Rectangle class. The width and height must be assigned
 to the value of size"""
    @property
    def size(self):
        return self.__size

"""Update the class Square by adding the public getter and setter size"""
    @size.setter
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