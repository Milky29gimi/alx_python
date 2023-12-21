""" squares """
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Square class inheriting from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): Size of the square.
            x (int, optional): x-coordinate of the square. Defaults to 0.
            y (int, optional): y-coordinate of the square. Defaults to 0.
            id (int, optional): Identifier for the object. Defaults to None.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        super().__init__(size, size, x, y, id)  # Calls the superclass constructor with required arguments

    @property
    def size(self):
        """
        Getter for size attribute.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size attribute.

        Args:
            value (int): The value to set for the size.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        self.width = value
        self.height = value