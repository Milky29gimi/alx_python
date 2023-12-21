import os    
    # Create the models package 
if not os.path.exists("models"):
    os.mkdir("models")
    with open("models/__init__.py", "w"):
        pass

class Base:
    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            # Increment __nb_objects and assign the new value to the public instance attribute id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects