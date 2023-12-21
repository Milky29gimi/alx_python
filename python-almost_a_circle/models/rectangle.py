"""create a class named Square that inherits from Rectangle """
from models.base import Base

class Rectangle(Base):
    """ define the class Square"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ define the class Square"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ define the class Square"""
        return self.__width

    @width.setter
    def width(self, value):
        """ define the class Square"""
        if value <= 0:
            raise ValueError("Width must be a positive number.")
        self.__width = value

    @property
    def height(self):
        """ define the class Square"""
        return self.__height

    @height.setter
    def height(self, value):
        """ define the class Square"""
        if value <= 0:
            raise ValueError("Height must be a positive number.")
        self.__height = value

    @property
    def x(self):
        """ define the class Square"""
        return self.__x

    @x.setter
    def x(self, value):
        """ define the class Square"""
        self.__x = value

    @property
    def y(self):
        """ define the class Square"""
        return self.__y

    @y.setter
    def y(self, value):
        """ define the class Square"""
        self.__y = value