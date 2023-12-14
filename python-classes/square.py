
# 0. Square with size

class Square:
    def __init__(self, size):
        self.__size = size

    def get_size(self):
        return self.__size

    def set_size(self, new_size):
        self.__size = new_size

    def area(self):
        return self.__size ** 2

    def perimeter(self):
        return 4 * self.__size

if __name__ == "__main__":
    d = Square(4)
    print(d.get_size)