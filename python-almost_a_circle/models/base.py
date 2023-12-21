"""Create the models package """   
class Base:
    """Private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            """Increment __nb_objects and assign the new value to the 
            public instance attribute id"""
            Base.__nb_objects += 1
            self.id = Base.__nb_objects