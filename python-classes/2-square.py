"""Area of a sqyare"""
class Square:
    """A class that defines a square.

    Attributes:
        __size (int): Represents the size of the square.
    """

    def __init__(self, size=0):
        """Initializes a Square instance with an optional size parameter.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If the size parameter is not an integer.
            ValueError: If the size parameter is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2