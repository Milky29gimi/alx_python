"""Only sub class of"""
def inherits_from(obj, a_class):
    """Checks if the object inherits (directly or indirectly) from the specified class.

    Args:
        obj: Any object.
        a_class: A class to compare against.

    Returns:
        bool: True if obj inherits from a_class (directly or indirectly), otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class