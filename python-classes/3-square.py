""" create a class called square
and define a private instance attribute calles size. 
Size validation- input validater"""

class Square:
      """
    This id a Square class.
    """
    def __init__(self, size=0):
        """ @__size:is a private instance attribut
        Size validation- input validater  """

        self.size = size


    @property
    def size(self):
        return self.__size
        """ @__size:is a private instance attribut
        Size validation- input validater  """

    @size.setter
    def size(self, value):
        """ @__size:is a private instance attribut
        Size validation- input validater  """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
            
            """ @__size:is a private instance attribut
        Size validation- input validater  """

        elif value < 0:
            raise ValueError("size must be >= 0")

            """ @__size:is a private instance attribut
        Size validation- input validater  """

        self.__size = value

    def area(self):
        return self.__size ** 2
        """ @__size:is a private instance attribut
        Size validation- input validater  """