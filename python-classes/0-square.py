# 0. Square with size

class Square:
    """
    This id a Square class.
    """
    def __init__(self, size):
        """
        @__size:is a private instance varible
        """
        self.__size = size

    # def get_size(self):
    #     return self.__size

    # def set_size(self, new_size):
    #     self.__size = new_size

    # def area(self):
    #     return self.__size ** 2

    # def perimeter(self):
    #     return 4 * self.__size


if __name__ == "__main__":
    my_square = Square(89)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)

