# ==================================================
# PYTHON ARITHMETIC OPERATORS
# ==================================================

# Arithmetic operators are used to perform
# mathematical calculations between two numbers.


# --------------------------------------------------
# 1. ADDITION OPERATOR (+)
# --------------------------------------------------
# Adds two numbers.
# Example: 1 + 2 = 3

a = 1
b = 2

res = a + b

print("Addition:", res) 
print(f"Addition using f-string: {res}")
print("Addition using format: {}".format(res))

# Output: 3


# --------------------------------------------------
# 2. SUBTRACTION OPERATOR (-)
# --------------------------------------------------
# Subtracts the second number from the first number.
# Example: 2 - 1 = 1

a = 2
b = 1

res = a - b

print("Subtraction:", res)
print(f"Subtraction using f-string: {res}")
print("Subtraction using format: {}".format(res))

# Output: 1


# --------------------------------------------------
# 3. MULTIPLICATION OPERATOR (*)
# --------------------------------------------------
# Multiplies two numbers.
# Example: 2 * 2 = 4

a = 2
b = 2

res = a * b

print("Multiplication:", res)
print(f"Multiplication using f-string: {res}")
print("Multiplication using format: {}".format(res))

# Output: 4


# --------------------------------------------------
# 4. DIVISION OPERATOR (/)
# --------------------------------------------------
# Divides the first number by the second number.
# Returns a float value, even if the result is a whole number.
# Example: 5 / 2 = 2.5

a = 5
b = 2

res = a / b

print("Division:", res)
print(f"Division using f-string: {res}")
print("Division using format: {}".format(res))

# Output: 2.5


# --------------------------------------------------
# 5. FLOOR DIVISION OPERATOR (//)
# --------------------------------------------------
# Divides two numbers and rounds the result DOWN
# to the nearest integer (for positive numbers).
# Example: 5 // 2 = 2

a = 5
b = 2

res = a // b

print("Floor Division:", res)
print(f"Floor Division using f-string: {res}")
print("Floor Division using format: {}".format(res))

# Output: 2


# --------------------------------------------------
# 6. MODULUS OPERATOR (%)
# --------------------------------------------------
# Returns the remainder after division.
# Example: 5 % 2 = 1

a = 5
b = 2

res = a % b

print("Modulus:", res)
print(f"Modulus using f-string: {res}")
print("Modulus using format: {}".format(res))

# Output: 1


# --------------------------------------------------
# 7. EXPONENTIATION / POWER OPERATOR (**)
# --------------------------------------------------
# Raises the first number to the power of the second number.
# Example: 2 ** 3 = 2 * 2 * 2 = 8

a = 2
b = 3

res = a ** b

print("Exponentiation:", res)
print(f"Exponentiation using f-string: {res}")
print("Exponentiation using format: {}".format(res))

# Output: 8


import sys
version = sys.version
print(version)  # Prints python version


#snake_casing
#Camel_Casing
