""" rectangles """
from models.base import Base

class Rectangle(Base):
    """
    Rectangle class inheriting from Base.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): x-coordinate of the rectangle.
        y (int): y-coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the rectangle. Defaults to 0.
            y (int, optional): y-coordinate of the rectangle. Defaults to 0.
            id (int, optional): Identifier for the object. Defaults to None.

        Raises:
            TypeError: If width, height, x, or y are not integers.
            ValueError: If width or height are less than or equal to 0, or if x or y are less than 0.
        """
        super().__init__(id)  # Call the superclass constructor with id

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area of the Rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the Rectangle instance with '#' in stdout.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """
        Overrides the string representation of the Rectangle object.

        Returns:
            str: String representation of the Rectangle object.
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        Updates attributes of the Rectangle using key-worded arguments.

        Args:
            *args (int): Arguments representing id, width, height, x, and y respectively.

        Keyword Args:
            **kwargs (int): Key-value pairs to update attributes.

        Raises:

Semira Hussien, [12/21/2023 7:22 PM]
TypeError: If any argument is not an integer.
        """
        if args:
            if len(args) != 5:
                raise IndexError("update expected 5 arguments")
            self.id, self.width, self.height, self.x, self.y = args
        else:
            for key, value in kwargs.items():
                if not isinstance(value, int):
                    raise TypeError(f"{key} must be an integer")
                setattr(self, key, value)