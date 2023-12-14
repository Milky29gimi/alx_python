"""Access and update private attribute"""
class Square:
    """A class that represents a square.

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
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square.

        Args:
            value (int): The size to set for the square.

        Raises:
            TypeError: If the value parameter is not an integer.
            ValueError: If the value parameter is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2