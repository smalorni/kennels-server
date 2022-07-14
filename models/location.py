class Location():
    """Creates class that defines properties on object
    """
    # Class initializer. It has parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address