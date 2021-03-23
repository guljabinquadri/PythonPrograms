#Functions in Python
a = 2
b = 4
c = sum((a,b)) #bulit in function which is already there in python
print(c)

#User define function (the function which is define by the user)
#for that we use "def" keyword and function name like "function1():"
def function1(): #we are not taking any input
    print("Helle World")
#print(function1())    #it will return "none"
function1() #for the singal time it will show 9thing
function1() #hello world
# now the def function will take input
def function2(a,b):
    print("Sum is", a+b)
function2(3,4)

def function3(c,d):
    average= (c+d)/2
    print(average)
    # returning
    return average
v = function3(2,6)
print(v)

#DocString
"""The docstring for a Python code object (a module, class, or function) is 
the first statement of that code object, immediately following the definition 
(the 'def' or 'class' statement)."""
#Example
def sum(a,b):
    """This is function to find out the sum""" #Docstring
    add = a+b
    return add
v = sum(10,5)
print(v)
#to print docs string
#print(name of the function.__doc__
print(sum.__doc__)


