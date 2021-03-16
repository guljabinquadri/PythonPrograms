#VARIBLES
var1="hello world" #string_varible
var2 = 6  #int_Varible
var3 = 6/6 #float_varible
var4=" there?"
#for knowing the type of the varible , we use type function
print(type(var1))
print(type(var2))
print(type(var3))
print(var2 + var3) #adding of this will be addition
print(var1 + var4) #adding of two string will be concatenate in the result
var5="56"
var6=" 64"
print(var5 + var6) #the result is 56 64 becoz both are string
""" For converting one variable to another varible we use typecasting"""
print(int(var5) + int(var6)) #now the result is 120 becoz the sting had converted to int.
""" different type of function of varible are
str(), int(), float"""
#For printing a string many times
print(10* "Guljabin\n")
#make a simple calculator that adds two number
print("Enter the 1st num")
inpnum1 = input()
print("Enter the 2nd num")
inpnum2 = input()
result = int(inpnum1) + int(inpnum2)
print("Sum of these two numbers is ",result)
