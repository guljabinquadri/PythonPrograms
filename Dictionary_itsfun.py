#Dictionary is nothing but key value pairs
#For dictionary we use {}
d1 = {}
print(type(d1)) # it will show <class 'dict'>
d2 = ()
print(type(d2)) #it will show <class 'tuple'>
d3 = []
print(type(d3)) # it will show <class 'list'>
d4 = {"Gul":"mub","srk":"gk","love":"hate"}
print(d4)
#print(d4["gul"]) # it will show error becoz it Gul(cast sensetive)
print(d4["Gul"])
#we can put dictionary,list,tuple in the place of value
#Dictionary inside a dictionary
d4 = {"Gul":{"mub":"jaan","tea":"coffee","book":"pen"},"srk":"gk","love":"hate"} #here the first vaule is called keys
print(d4["Gul"])
print(d4["Gul"]["tea"])
#adding values in dictionary
d4["cat"] = "dog"
d4.update({"pull":"push"})
print(d4)
del d4["Gul"] # deleting values from dictionary
print(d4)
#copy
d5= d4  #value of d5 will copy value of d6
del d5["love"]
print(d4)
#if you dont want the value to be copied then we use
d5 = d4.copy()
del d5["srk"]
print(d4)
d4 = {"Gul":{"mub":"jaan","tea":"coffee","book":"pen"},"srk":"gk","love":"hate"}
print(d4.keys())
print(d4.items()) #.items prints the key value pairs

#For function goggle dictionary function in python
