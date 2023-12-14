""" create a class called square
and define a private instance attribute calles size. 
Size validation- input validater 
the area () method claculates the area of the square by multipling."""

class Square:
      """
    This id a Square class.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
    