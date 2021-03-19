var1 = 2
var2 = 23
var3 = int(input())

if var3>var2:
    print("Greater")
elif var3==var2:
    print("Equal")
else:
    print("Lesser")

#to check a num/string is in or not the list
list1 = [2, 3, 4, 5]
print(5 in list1)
print(5 not in list1)

#take age as as input and say if a person is eligible for driving or not
print("What is your age")
age = int(input())

if age>18:
    print("You are eligible for driving")
elif age==18:
    print("Come to our office to check your eligibility")
else:
    print("You are not eligible")
    

