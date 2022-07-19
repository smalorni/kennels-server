class Employee():
    """Creates class that defines properties on object
    """
    # Class initializer. It has parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, address, location_id):
        self.id = id
        self.name = name
        self.address = address
        self.location_id = location_id
        #self.location = None