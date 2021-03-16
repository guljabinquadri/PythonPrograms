"""Lists ans list function"""
grocery = ["coffee","tea","soap","sweets", 54]
print(grocery)
# Finding the postion/index of the list
print(grocery[0])
print(grocery[3])
numbers = [56, 4, 37, 0, 799]
print(numbers)
print(numbers[0])

# For sorting the list, sort() function along will return none so we have to print it after sort()
print(numbers.sort())# it will sort in ascending order
print(numbers)
print(numbers.reverse()) # it will reverse the list
print(numbers)
print(numbers[0])
"""Slicing"""
num = [56, 4, 37, 0, 799]
print(num[0:])
print(num[:])
print(num[1:3])
print(num[::2])
print(num[::-1])
"""always tale -1 in -ve slicing dont take more than it like -2, -3 etc becoz it will show error"""
print(len(num))
print(max(num))
print(min(num))
"""Append function  means it add a number at the end"""
num = [56, 4, 37, 0, 799]
num.append(23)
print(num)
num =[]
num.append(23)
num.append(27)
num.append(66)
print(num)
"""insert fun :- if uh want to insert a number in ant position/index eg:-num.insert(2, 222) 
the poistion will tell which index to be replace and the 2nd will tell by which number it will be replace"""
num=[1, 2, 3, 4, 5]
num.insert(3, 69)
print(num)
num=[1, 2, 3, 4, 5]
num.remove(4) #removing a number
print(num)
num=[1, 2, 3, 4, 5]
num.pop() # it will remove the last num
print(num)

"""Tupel Function(tp uses parenthesis() instead if [] and it is immutable which value can not be changed"""
#mutable- can change
#immutable - can not change
"""tp = (1, 3, 4)
print(tp)
tp = (1, 3, 4)
tp[1] = 2
print(tp)""" #it will show error becoz tuple value can not change
tp = (1)
print(tp) #it will show 1 without ()
# for getting a (1) in the single digit we use:-
tp =(1,)
print(tp)
# for interchanging two varibales with a temp num
a = 10
b= 20
temp = a
a = b
b = temp
print(a, b)
# but in python it is
a = 30
b = 12
a, b = b, a
print(a, b)

"""Search python list function"""
