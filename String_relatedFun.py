name = "Guljabin"
print(name[6])
#if uh want to write Gul
print(name[0:3]) #here we dont write 0:2 becoz in str index, it will include 0 but exculde 2
#for knowing the length we use len() function
print(len(name))
print(name[0:78]) # it will still give the result becoa it is greater then the total len
print(name[0:]) # if uh will leave the end one it will take the full len str
print(name[:8])# it will take the staring part as 0 always
"""If you want to skip one character in between """
print(name[0:8:2])
print(name[0::2])
print(name[::]) #it take the defualt value:- name[0:8:1]
"""If you want to skip two character in between """
print(name[::3])
""" negative index/str slicling """ #refer notes
print(name[::-1]) # reverse the string
print(name[::-2]) #reverse the string then skip 1 character in between
"""Different function"""
print(name.isalnum()) #it will show true if the string is without space
print(name.isalpha())
print(name.endswith("en"))
print(name.count("i")) #how many time the character occurs
print(name.capitalize()) #it will capitalize the 1st letter of the sentence
print(name.find("l")) #it will show the index number of the word/letter
print(name.lower())
print(name.upper())
"""Replacing a word with others, the 1st word is replaced by the 2nd"""
print(name.replace("u", "a"))

"""For more details go search string function"""
