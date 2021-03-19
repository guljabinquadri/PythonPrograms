# Sets
s = set()
print(type(s))
#list inside a set is shown as a <class 'set'>
set_list = set([2,3,4])
print(set_list)
print(type(set_list))
#adding elements in set
s.add(1)
s.add(1)#it will till print {1} becoz a set redime a unique value
s.add(2)
print(s)
s.union({2,3})
s1 = s.intersection({2,3})
print(s,s1)
#Disjoint function
s2 ={1,2,3}
s3 ={3,4,5}
print(s2.isdisjoint(s3))
#remove
s.remove(1)
print(s)
#you can google more about sets

