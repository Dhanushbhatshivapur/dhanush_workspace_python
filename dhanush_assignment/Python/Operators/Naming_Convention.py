
#Naming Conventions in python


# 1. Snake Case
# Recommended for Python variables and functions
# - All letters are lowercase.
# - Words are separated using underscores _.

# Example: Snake Case

first_name = "John"
last_name = "David"
employee_salary = 25000

print(first_name)
print(f"Employee Salary: {employee_salary}")
print("Last Name: {}".format(last_name))


#-------------------------------------------------------------------------------------

# 2. Camel Case
# - First word starts with a lowercase letter.
# - Every subsequent word starts with an uppercase letter.
# - No spaces or underscores.

# Example: Camel Case

firstName = "John"
lastName = "David"
employeeSalary = 25000

print(firstName)
print(f"Employee Salary: {employeeSalary}")
print("Last Name: {}".format(lastName))


#-------------------------------------------------------------------------------------


# 3. Pascal Case
# - Every word starts with an uppercase letter.
# - No spaces or underscores.
# - Commonly used for Python class names.

# Example: Pascal Case


class EmployeeDetails:
    pass

class StudentInformation:
    pass

print(EmployeeDetails.__name__)
print("Class Name: {}".format(StudentInformation.__name__))

#-------------------------------------------------------------------------------------

# 4. Upper Case (Constant Naming)
# - All letters are uppercase.
# - Words are separated by underscores.
# - Commonly used for constants.
# Example: Upper Case

PI_VALUE = 3.14159
MAX_LIMIT = 100
COMPANY_NAME = "Google"

print(PI_VALUE)
print(f"Maximum Limit: {MAX_LIMIT}")
print("Company Name: {}".format(COMPANY_NAME))



#-------------------------------------------------------------------------------------

# 5. Leading Underscore
# - A single underscore before a variable or method.
# - Indicates that it is intended for internal use.
# - It is a convention, not a restriction.

# Example: Leading Underscore

_employee_name = "John"
_internal_salary = 25000

print(_employee_name)
print(f"Internal Salary: {_internal_salary}")
print("Employee Name: {}".format(_employee_name))


#-------------------------------------------------------------------------------------

# 6. Double Leading Underscore
# - Two underscores before an attribute inside a class.
# - Triggers name mangling in Python.
# - Helps avoid accidental name conflicts in subclasses.

# Example: Double Leading Underscore

class Employee:

    def __init__(self):
        self.__salary = 25000


emp = Employee()

# Access through the name-mangled attribute
print(emp._Employee__salary)

