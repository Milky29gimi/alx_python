class Square:
    def __init__(self, size):
        self.__width = 0
        self.__height = 0
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value <= 0:
            raise ValueError("Size must be a positive number.")
        self.__width = value
        self.__height = value
        self.__size = value

    def get_area(self):
        return self.__width * self.__height