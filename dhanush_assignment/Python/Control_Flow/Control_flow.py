

age = 18

if age >= 18 : 
    print("Eligible to vote") #pass

else:
 print("Ineligible to vote")


marks  = 35
if marks>= 40:    #did not satisfied the condition
   print("passed")

print("Program Passed")   #pass




marks = 50   #35 
if marks >= 90:   # 35 >= 90 so this condition fails
   print("Grade A")
elif marks >=80:
   print("Grade B")
elif marks >=65:
   print("Grade C")
elif marks >= 40:
   print("Grade D")
else:
   print("F")  # pass

    

if 40 <= marks <= 100:
    print("Pass")


#Python code for date range
#| Condition | Range of marks | Grade |
#| --- | --- | --- |
#| `90 <= marks <= 100` | 90–100 | A |
#| `80 <= marks < 90` | 80–89.99 | B |
#| `65 <= marks < 80` | 65–79.99 | C |
#| `40 <= marks < 65` | 40–64.99 | D |
#| `marks < 40` | Below 40 | F |


# Nested > condition inside the condition : "Nested condition"
# A nested loop in Python is simply a loop placed inside another loop
#start >>  check cond >> false >> True >>check condition

#if condition1 : >> True
    #if condition2 :  Enters to this block >> True
       #statement 1 
    #else:
       #statement 2 Skips this statement
#else:
#statement 3


#ternery condition : all the condition >> if , elif all of these statement will



#ternery  we use in rare case
#value_is_true if condition else value_is_false
##age = 20
# list comprehension methods , tuple ##


#we can use nested loop ternery format

marks = 75

if marks >= 40:
    if marks >= 80:
        print("Excellent")
    else:
        print("Pass")
else:
    print("Fail")



# " " Empty space is a vlid string


#empty space is considered to be non valid
name = " "  #empty string is valid 
if name : 
   print("Name is present")
else:
   print("Name is missing")






#nested loops
marks = 75

if marks >= 40:
    if marks >= 80:
        print("Excellent")
    else:
        print("Pass")
else:
    print("Fail")





#nested ternery loops
marks = 75

result = "Fail" if marks < 40 else ("Excellent" if marks >= 80 else "Pass")

print(result)

