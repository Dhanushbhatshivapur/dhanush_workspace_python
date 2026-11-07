#  Membership Operators
# Used to check whether an element exists inside a string, list, tuple, etc.

text = "Python"

print("P" in text)       # True
print("z" in text)       # False
print("z" not in text)   # True


# Identity Operators
# Python has two identity operators:
# - is
# - is not
# They check whether two variables refer to the same object, not simply whether their values are equal.

a = [10, 20, 30]
b = [10, 20, 30]

print(a == b)  # True
print(a is b)  # False


# Identity Operators – IS and IS NOT
# Identity operators check whether two variables refer to the same object in memory.

# There are two identity operators:
# Operator	Meaning
# is	Checks whether both refer to the same object
# is not	Checks whether both refer to different objects

# Identity Operator: IS

a = [10, 20, 30]
b = a

# Both variables refer to the same list object.
print(a is b)  # True


# Identity Operator: IS NOT

x = [10, 20, 30]
y = [10, 20, 30]

# Both lists have equal values but are different objects.
print(x is not y)  # True






#Difference between == and is

a = [10, 20, 30]
b = [10, 20, 30]

# == compares values.
print(a == b)  # True

# is compares object identity.
print(a is b)  # False



# ============================================================
# 6. MEMBERSHIP OPERATORS
# ============================================================

language = "Python"

print("P" in language)       # True: P exists in the string
print("z" not in language)   # True: z does not exist

fruits = ["apple", "banana", "mango"]
print("banana" in fruits)    # True


# ============================================================
# 7. IDENTITY OPERATORS
# ============================================================

first_list = [1, 2, 3]
second_list = [1, 2, 3]
third_list = first_list

print(first_list == second_list)  # True: same contents
print(first_list is second_list)  # False: different objects
print(first_list is third_list)   # True: same object

# == compares values. "is" checks whether both names refer
# to the exact same object in memory.