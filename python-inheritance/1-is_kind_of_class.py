"""Same class or inherit from"""
def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of, or if it's inherited from, the specified class.

    Args:
        obj: Any object.
        a_class: A class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or inherited from it, otherwise False.
    """
    return isinstance(obj, a_class)