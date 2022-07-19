import sqlite3
import json
from models import Employee
from models.location import Location

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
        """Get all employees from list"""
        # Open a connection to the database
        with sqlite3.connect("./kennel.sqlite3") as conn:

            # Just use these. It's a Black Box.
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # Write the SQL query to get the information you want
            db_cursor.execute("""
            SELECT
                a.id,
                a.name,
                a.address,
                a.location_id,
                l.name location_name,
                l.address location_address
            
            FROM employee a
            JOIN Location l
                ON l.id = a.location_id
            """)

            # Initialize an empty list to hold all employee representations
            employees = []

            # Convert rows of data into a Python list
            dataset = db_cursor.fetchall()

            # Iterate list of data returned from database
            for row in dataset:

                # Create an employee instance from the current row.
                # Note that the database fields are specified in
                # exact order of the parameters defined in the
                # Employee class above.
                employee = Employee(row['id'], row['name'], row['address'], row['location_id'])

                # Create Location instance from current row
                location = Location(row['id'], row['location_name'], row['location_address'])

                # Add dictionary representation of location to employee
                employee.location = location.__dict__

                employees.append(employee.__dict__)

        # Use `json` package to properly serialize list as JSON
        return json.dumps(employees)

def get_single_employee(id):
        """Get single employee from list"""
        with sqlite3.connect("./kennel.sqlite3") as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # Use a ? parameter to inject a variable's value
            # into the SQL statement.
            db_cursor.execute("""
            SELECT
                a.id,
                a.name,
                a.address,
                a.location_id
            FROM employee a
            WHERE a.id = ?
            """, ( id, ))

            # Load the single result into memory
            data = db_cursor.fetchone()

            # Create an employee instance from the current row
            employee = Employee(data['id'], data['name'], data['address'], data['location_id'])

            return json.dumps(employee.__dict__)
    
def create_employee(new_employee):
    """Create new employee"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Employee
            ( name, address, location_id )
        VALUES 
            ( ?, ?, ?);
        """, (new_employee['name'], new_employee['address'],
              new_employee['location_id'], ))

        id = db_cursor.lastrowid

        new_employee['id'] = id

    return json.dumps(new_employee)

# Delete employee from list
def delete_employee(id):
    """Delete employee from list"""
    # Initial -1 value for employee index, in case one isn't found
    employee_index = -1

    # Iterate the EMPLOYEES list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Store the current index.
            employee_index = index

    # If the employee was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

# Update employees from list
def update_employee(id, new_employee):
    """Update employee from list"""
    # Iterate the EMPLOYEES list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Update the value.
            EMPLOYEES[index] = new_employee
            break

# Get employees by location
def get_employees_by_location(location):
    """Get Employee by Location"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            e.id,
            e.name,
            e.address,
            e.location_id
        from Employee e
        WHERE e.location_id = ?
        """, ( location, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
            employees.append(employee.__dict__)

    return json.dumps(employees)