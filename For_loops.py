#For loops

list1 = ["Harry", "Larry", "Marry"]
for item in list1:
    print(item)

# For loop in list
list2 = [ ["Larry",18], ["Harry",19], ["Sarry",21] ]
for item in list2:
    print(item)
for item, age in list2:
    print(item, "and their age is", age)

#for in dictinoery
dict1 = dict(list2)
print(dict1)
"""for item, age in dict1: # it will show error in the dict case
    # but if we will write dict1.items() then it will work
    print(item, age)"""
for item, age in dict1.items():
    print(item, "is", age)
# for geeting only the key value then
for item in dict1:
    print(item)
