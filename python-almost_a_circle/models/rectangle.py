"""create a class named Rectangle that inherits from Base """
class Rectangle:
    """ define the class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = None
        self.__height = None
        self.__x = None
        self.__y = None
        self.set_width(width)
        self.set_height(height)
        self.set_x(x)
        self.set_y(y)
        self.id = id

    def get_width(self):
        return self.__width

    def set_width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        return self.__width * self.__height

    def display(self):
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.set_width(args[1])
            if len(args) >= 3:
                self.set_height(args[2])
            if len(args) >= 4:
                self.set_x(args[3])
            if len(args) >= 5:
                self.set_y(args[4])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"