str = "python"

print(str[1])

print(str[-5])

print(str[0:2])  # it will skip the toppest index

#print(str[-1:-2])
print(str[-1:-3])
print(str[::-1])  #slicer
#print(str.substring[1:4])


str1 = "india"
print(str1[1:4:2]) #in positive indexing the topmost value
#will be fixed #every second index will be skipped



nums = [0,1,2,3,4,5,6]
print(nums[1:5:2])

#S : 1
#E : 5

str = "python"
print(str[-1]+str[1:4])    # concatination


#step function
#slicing # concatination

# chapter 3 : String methods - finding the text values, built in function
#length(), upper(), lower(), find(), count
#cannot write the variable name as count , length

str = "PYThon"
print(str.lower())  # converting the strong to lower case

# upper() converts the strong to upper case
str = "python"
print(str.upper())

#strip
str





#strip removes the space from the String (leading space /trailing space)
str = "python "
print(str.strip())


# replace ()   // removes / replace the part of the string
str = "I love Java"
print(str.replace("Java","Python"))  # repalce ("string1","string2")


#split()  >> The split() method splits a string into a list.
txt = "welcome to the jungle"
x = txt.split()
#print(x)
#print(x[1:3])
#print(x.find("welcome"))



#find()  find the index in the strong
str = "apple banana apple cherry"
print(str.find("apple",5))   # index of the characters 
print(str.find("apple"))   # index of the characters 

print(str.count("apple")) #count() count the number of strings

name = "Dhanush"
age = 28
city = "Belgaum"
print(f"My name is {name}, My age is {age} and I am from {city}")  #passing f string



name = "Dhanush"
age = 28
city = "Belgaum"
print("My name is {}, My age is {} and I am from {}".format(name,age,city)) #format



# String concatination joing the strings together

first_name = "Dhanush"
last_name = "Shivapur"
print(first_name +" "+ last_name)
print (f"My name is {first_name} {last_name}")
#print("My name is {}, My age is {} and I am from {}".format(first_name,last_name)) #format




#When you multiply an integer by a float, Python returns a float.
quantity = int("2")
unit_price = float("1250.50")
order_total = quantity * unit_price
print("Order total: " + str(order_total),type(order_total)) # int * float = float
# float has 24 bytes value which can store string









