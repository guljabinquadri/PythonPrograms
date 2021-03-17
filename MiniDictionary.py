#Create a dictionary and take the input from the user and return the result from the dictionary
d1 = {"data":"Data are units of information, often numeric, that are collected through observation.",
      "stack": "Stack is a linear data structure which follows a particular order in which the operations are performed.",
      "class":" a class is an extensible program-code-template for creating objects, providing initial values for state.",
      "method": "method in object-oriented programming (OOP) is a procedure associated with a message and an object."}
print("Enter the word you want to search")
instr = input()
print(d1[instr])
