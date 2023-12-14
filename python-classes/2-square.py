""" create a class called square
and define a private instance attribute calles size. 
Size validation- input validater 
the area () method claculates the area of the square by multipling."""

class Square:
      """
    This id a Square class.
    """
    def __init__(self, size=0):
        """ @__size:is a private instance attribut
        Size validation- input validater  """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
            """ @__size:is a private instance attribut
        Size validation- input validater  """

        elif size < 0:
            raise ValueError("size must be >= 0")
            """ @__size:is a private instance attribut
        Size validation- input validater  """

        self.__size = size
        """ @__size:is a private instance attribut
        Size validation- input validater  """
        

    def area(self):
        return self.__size ** 2
        """ @__size:is a private instance attribut
        Size validation- input validater  """
    