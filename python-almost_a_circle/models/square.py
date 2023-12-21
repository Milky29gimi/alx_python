"""create a class named Square that inherits from Rectangle """
from models.rectangle import Rectangle

class Square(Rectangle):
    """ define the class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """ define the class Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ define the class Square"""
        return self.width

    @size.setter
    def size(self, value):
        """ define the class Square"""
        self.width = value
        self.height = value

    @property
    def area(self):
        """ define the class Square"""
        return self.width * self.height   

    def __str__(self):
        """ define the class Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"