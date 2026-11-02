#Basic assignemnt xvalue
#Assignment operators 
#Assignment operators are used to assign the values to the variables



x = 10
print (x)

#Add and     assign value to x
x = 10
x +=5
print (x)   #x = x+5 (10 + 5)

#Substract  and Assign value to x
x = 10
x -= 5
print(x)  #x= x-5 (10-5 = 5)

#Multiple and assign value to x
x = 10
x*= 5
print (x)  #10*5 = 50

#Power/Exponent


#Divide and assign value to x
x = 50
x /= 5  # x = x/5 (50/5) = 10.0  Quotient printed in Float
print(x)

#Floor Division and assign to value to x
x = 50
x //=5
print (x)  # Floor division Hence quotient is printed in Integer





# ==========================================
# Assignment Operators in Python
# ==========================================

# Operator | Example | Same as
# ------------------------------------------
#    =    | x = 10  | x = 10
#    +=   | x += 5  | x = x + 5
#    -=   | x -= 5  | x = x - 5
#    *=   | x *= 5  | x = x * 5
#    /=   | x /= 5  | x = x / 5
#    %=   | x %= 5  | x = x % 5
#   **=   | x **= 5 | x = x ** 5
#   //=   | x //= 5 | x = x // 5


print(f"Division :", 7 / 3)          # always a float # Output : Division : 2.3333333333333335
print(round(7 / 3, 2))  #round to 2  #Output :  2.33
print(f"Division rounded to 2: {round(7 / 3, 2)}")     #Output : Division rounded to 2: 2.33
print(7 // 3)           # full boxes #Output : 2
print(7 % 3)            # items left over #Output : 1
print(2 ** 10)          # power  #Output : 1024
print((100 + 50) * 2)   # brackets first  #Output : 150 * 2 = 300


# ==========================================
# 1. Assignment Operator (=)
# ==========================================

x = 10

print("Assignment:", x)   
print(f"Assignment printing using f-string: {x}")
print("Assignment printing using format: {}".format(x))


# ==========================================
# 2. Addition Assignment (+=)
# Same as: x = x + 5
# ==========================================

x = 10
x += 5

print("Addition:", x)  
print(f"Addition printing using f-string: {x}")
print("Addition printing using format: {}".format(x))


# ==========================================
# 3. Subtraction Assignment (-=)
# Same as: x = x - 5
# ==========================================

x = 10
x -= 5

print("Subtraction:", x)
print(f"Subtraction printing using f-string: {x}")
print("Subtraction printing using format: {}".format(x))


# ==========================================
# 4. Multiplication Assignment (*=)
# Same as: x = x * 5
# ==========================================

x = 10
x *= 5

print("Multiplication:", x)
print(f"Multiplication printing using f-string: {x}")
print("Multiplication printing using format: {}".format(x))


# ==========================================
# 5. Division Assignment (/=)
# Same as: x = x / 5
# ==========================================

x = 10
x /= 5

print("Division:", x)
print(f"Division printing using f-string: {x}")
print("Division printing using format: {}".format(x))

# ==========================================
# 6. Floor Division Assignment (//=)
# Same as: x = x // 5 
# ==========================================

x = 10
x //= 5

print("Floor Division:", x)
print(f"Floor Division printing using f-string: {x}")
print("Floor Division printing using format: {}".format(x))


# ==========================================
# 7. Modulus Assignment (%=)
# Same as: x = x % 5
# ==========================================

x = 10
x %= 5

print("Modulus:", x)
print(f"Modulus printing using f-string: {x}")
print("Modulus printing using format: {}".format(x))


# ==========================================
# 8. Exponentiation Assignment (**=)
# Same as: x = x ** 5
# ==========================================

x = 2
x **= 5

print("Exponentiation:", x)
print(f"Exponentiation printing using f-string: {x}")
print("Exponentiation printing using format: {}".format(x))


