EMPLOYEES = [
    {
            "id": 1,
            "name": "Jon Snow",
        },
        {
            "id": 2,
            "name": "Lucille Johnson",
    }
]

def get_all_employees():
    """Invoke function and returns list of employees"""
    return EMPLOYEES

# Function with a single parameter
def get_single_employee(id):
    """Function to locate single employee, return the requested employee"""
    # Variable to hold the found location, if it exists
    requested_employee = None

    # Iterate the EMPLOYEES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee
    return requested_employee
    
def create_employee(employee):
    """Add employee to list"""
    # Get the id value of the last animal in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    employee["id"] = new_id

    # Add the animal dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee
