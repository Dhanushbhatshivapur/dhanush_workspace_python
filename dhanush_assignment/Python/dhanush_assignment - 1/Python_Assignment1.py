#Variables and Naming Conventions
#Q1. Create variables to store the following information about yourself:
name = 'Dhanush N Shivapur'
age = 29
city = "belgaum"
height =  6

print(f"My name is {name}, my age is {age}, I am from {city}, and my height is {height}.")

#Q2. Create variables using meaningful names to store 
#the price of a product, quantity purchased, and customer name. Print all three.

product_price = 20
quantity_purchased = 30 
customer_name = 'oracle'

print(f"Product price : ${product_price}")
print(f"Quanity purchased :  {quantity_purchased} Pieces")
print(f"Customer name: {customer_name}")

#Q3. Predict the output:
x = 10
y = x
x = 25

print(x) #10  y is assigned with the value x
print(y) #25 x is assigned with the latest value


#------------------------------------------------------------------------------------------



"""Data Types"""   #DocString : is a String literal that are passed as statements in the 
#Docstrings in Python are stored as metadata inside runtime objects and retained in memory
#A string literal is a sequence of characters enclosed in quotation marks that represents a fixed text value directly in source code

#Data Types : Different Values are assigned in the variable
#Variables need to be created with a proper naming format
#A variable is a name that refers to a value. Creating one with = is called assignment.

#Q1. Create one variable for each of these data types:

# ==========================================
# Python Data Types
# ==========================================

# 1. Integer (int)
age = 28

# 2. Decimal Number (float)
salary = 25000.50

# 3. Text (str)
name = "Python"

# 4. Boolean (bool)
is_employed = True


# ==========================================
# Printing Values and Data Types
# ==========================================

# Integer
print("Integer:", age, type(age))
print(f"Integer using f-string: {age}, {type(age)}")
print("Integer using format: {}, {}".format(age, type(age)))


# Float
print("Float:", salary, type(salary))
print(f"Float using f-string: {salary}, {type(salary)}")
print("Float using format: {}, {}".format(salary, type(salary)))


# String
print("String:", name, type(name))
print(f"String using f-string: {name}, {type(name)}")
print("String using format: {}, {}".format(name, type(name)))


# Boolean
print("Boolean:", is_employed, type(is_employed))
print(f"Boolean using f-string: {is_employed}, {type(is_employed)}")
print("Boolean using format: {}, {}".format(is_employed, type(is_employed)))





# Q2. Predict the output:


a = 10
b = 3.5
c = "Python"
d = True

print(type(a))   #Output  : <class 'int'>
print(type(b))   # Output : <class ' float'>
print(type(c))   #Output : <class 'str'>
print(type(d))    #Output  :  <class 'bool'>



#Type Conversion
x = "250"
y = int(x)

print(y)  #y stores the value of string x converted to integer 
print(type(y))  # type int


# 3. What is the difference between the following?
# Print their data types and explain the difference.
a = 25  # Output :  <class 'int'>
b = "25" #Output : <class 'str'>







# Arithmetic Operations
# Q1. Take two numbers and display their:

a = 20
b = 5

print(a + b)   # Output: 25 (Addition)
print(a - b)   # Output: 15 (Subtraction)
print(a * b)   # Output: 100 (Multiplication)
print(a / b)   # Output: 4.0 (Division)
print(a // b)  # Output: 4 (Floor Division)
print(a % b)   # Output: 0 (Modulus / Remainder)
print(a ** b)  # Output: 3200000 (Exponentiation)







#Q2. Predict the output

a = 17
b = 5

print(a / b)   # Output: 3.4
print(a // b)  # Output: 3
print(a % b)   # Output: 2
print(a ** 2)  # Output: 289


# Operator	             Meaning	                                              Result
#   /	            Division – returns quotient as a float	                            3.4
#  //	        Floor division – rounds quotient down to the nearest integer	        3
#  %            	Modulus – returns the remainder	                                    2
#  **	           Exponentiation – raises a number to a power	                 17**2 = 17*17 = 289







#Q3. Calculate the total purchase price

# Given:

# Product price = ₹250

# Quantity = 4

# Calculate and print the total amount.

product_price = 250
quantity = 4

total_amount = product_price * quantity

print("Total amount:", total_amount)  # Output: Total amount: 1000
print("Total amount in float: ₹",float(total_amount))  #Output : Total amount : ₹1000
print(f"Total amount using f string: ₹{total_amount}") #Output : ₹1000 using fstring
print("Total amount using format print built in function: ₹{}".format(total_amount))  #Output : ₹1000 using .format string built in operator


print(f"Division :", 7 / 3)          # always a float # Output : Division : 2.3333333333333335
print(round(7 / 3, 2))  #round to 2  #Output :  2.33
print(f"Division rounded to 2: {round(7 / 3, 2)}")     #Output : Division rounded to 2: 2.33
print(7 // 3)           # full boxes #Output : 2
print(7 % 3)            # items left over #Output : 1
print(2 ** 10)          # power  #Output : 1024
print((100 + 50) * 2)   # brackets first  #Output : 150 * 2 = 300










# Q4. Write a program to calculate the average of three numbers.

# Use the values 75, 80, and 95.

a = 75
b = 80
c = 95

total = a + b + c  # Output: 250

average = total / 3  # Output: 83.33333333333333

print("Total:", total)       # Output: Total: 250
print("Average:", average)   # Output: Average: 83.33333333333333
print("Average round of to 3 : ",round(average,3)) #Output Average round of to 3 : 83.333


print(f"Average rounded to 3 decimal places using fstring: {round(average, 3)}")
#Average rounded to 3 decimal places using fstring: 83.333


print("Average rounded to 3 decimal places using format(): {}".format(round(average, 3)))
# Output: Average rounded to 3 decimal places using format(): 83.333