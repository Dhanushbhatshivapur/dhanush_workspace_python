
# ( "32"(2**5) "16"(2**4)  "8"(2**3) "4"(2**2) "2"(2**1) "1"(2**0))


a = 5 #0101 (8421)  decimal to binary  (each bit place is power of 2)
b = 4 #0100 
print(a & b)  #0001 (1)


print (a & b >> 1)
print (a & b << 1)

a = 5  #0101  # Shifting by 1 bit
print ( a>>1) #5//2**1 = "2" (0010)   // 5(0101)>> 2(0010)  shifting the bit right side by 1
print (a<<1) #5*2**1 = "10" (1010)  //5(0101) << 10(1010) shifting the bit left side by 2

a = 5 #0101  # SHifting by 2 bit
print ( a>>2) #5//2**2 = "1" (0010)   // 5(0101)>> 2(0010)  shifting the bit right side by 1
print (a<<2) #5*2**2 = "20" (10100)  //5(0101) << 10(1010) shifting the bit left side by 2


#General Rule: Right-shifting a number by n bits (a >> n) is 
#equivalent to  a // 2**n  for non-negative numbers.

#Right Shift
#Formula: a>>n = (a//2**n)  //Right Shift by n bit

# Left Shift
#Formula: a << n = (a*2**n)  //Left Shift by n bit



# >> value //2   // right shift by 1 bit
# << value * 2  // left shift by 1 bit












