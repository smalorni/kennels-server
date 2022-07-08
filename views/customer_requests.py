CUSTOMERS = [
    {
            "id": 1,
            "name": "Seth Watson",
        },
        {
            "id": 2,
            "name": "MaryAnn Shaffer",
    }
]

def get_all_customers():
    """Invoke function and returns list of customers"""
    return CUSTOMERS

# Function with a single parameter
def get_single_customer(id):
    """Function to locate single customer, return the requested customer"""
    # Variable to hold the found location, if it exists
    requested_customer = None

    # Iterate the Customers list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer
    return requested_customer

def create_customer(customer):
    """Add customer to list"""
    # Get the id value of the last animal in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    customer["id"] = new_id

    # Add the animal dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer
