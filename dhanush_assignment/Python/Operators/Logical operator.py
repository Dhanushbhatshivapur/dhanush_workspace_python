#Python – Logical Operators (AND, OR, NOT)

#What are logical operators?
# Logical operators are used to combine two or more conditions and return a Boolean result (True or False).

# Python has three main logical operators:
# 1. and
# 2. or
# 3. not



# 1. AND Logical Operator
# Definition: The and operator returns True only when BOTH conditions are True. If even one condition is False, the result will be False.

# AND Truth Table
# Condition 1	Condition 2	Result
# True	True	True
# True	False	False
# False	True	False
# False	False	False



# Example 1: Basic AND operation
# AND Logical Operator
# Rule: Both conditions must be TRUE.

print(True and True)      # Output: True
print(False and False)    # Output: False
print(True and False)     # Output: False
print(False and True)     # Output: False

# Example 2: Using Boolean variables
# Creating two Boolean variables

age_valid = True
is_valid = True

# AND checks whether both variables are True.

print(age_valid and is_valid)  # Output: True

#Example 3: When one condition is False
# Creating Boolean variables

age_valid = True
is_valid = False

# Checking both conditions using AND.

print(age_valid and is_valid)  # Output: False


#Example 4: Real-world application
# Login validation example

is_email_valid = True
is_password_valid = True

# Login is successful only when BOTH are valid.

if is_email_valid and is_password_valid:
    print("Login successful")
else:
    print("Invalid email or password")





#---------------------------------------------------------------------------

# 2. OR Logical Operator
# Definition: The or operator returns True when AT LEAST ONE condition is True. It returns False only when both conditions are False.

# OR Truth Table
# Condition 1	Condition 2	Result
# True	True	True
# True	False	True
# False	True	True
# False	False	False


# OR Logical Operator
# Rule: At least ONE condition must be TRUE.

#Example 1: Basic OR operation
print(True or True)       # Output: True
print(False or False)     # Output: False
print(True or False)      # Output: True
print(False or True)      # Output: True


# Creating two Boolean variables

is_email = True
is_valid = True

# OR checks whether at least one variable is True.


#Example 2: Using Boolean variables
print(is_email or is_valid)  # Output: True


#Example 3: When only one condition is True
# Creating Boolean variables

is_email = True
is_valid = False

# OR returns True because one condition is True.

print(is_email or is_valid)  # Output: True

#Example 4: When both conditions are False

is_email = False
is_valid = False

# Both conditions are False.

print(is_email or is_valid)  # Output: False


#Example 5: Real-world application
# Login using email OR mobile number

is_email_valid = False
is_mobile_valid = True

# User can proceed if either method is valid.

if is_email_valid or is_mobile_valid:
    print("Login allowed")
else:
    print("Login denied")










#--------------------------------------------------------------------------------------

# 3. NOT Logical Operator
# Definition: The not operator reverses the Boolean value.
# - True becomes False.
# - False becomes True.
# NOT Truth Table
# Condition	Result
# True - False
# False - True

# NOT Logical Operator
# Rule: Reverse the Boolean value.

#Example 1: Basic NOT operation
# NOT Logical Operator
# Rule: Reverse the Boolean value.

print(not True)    # Output: False
print(not False)   # Output: True

#Example 2: Using Boolean variables
# Creating a Boolean variable

is_logged_in = True

# NOT reverses the current value.

print(not is_logged_in)  # Output: False




#Example 3: When the variable is False
is_logged_in = False

print(not is_logged_in)  # Output: True




#Example 4: Real-world application
# Checking whether a user is NOT logged in.

is_logged_in = False

if not is_logged_in:
    print("Please login to continue")
else:
    print("Welcome back")




# User eligibility validation

age = 25
is_email_verified = True
is_blocked = False

# AND: Age and email verification must both be valid.
# NOT: User must NOT be blocked.

if age >= 18 and is_email_verified and not is_blocked:
    print("User is eligible")
else:
    print("User is not eligible")

