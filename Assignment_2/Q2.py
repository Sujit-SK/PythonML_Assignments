a = 10
b = 10

print(id(a))
print(id(b))
print(id(a) == id(b))
#Ans : int is immutable cannot change. 
# interned for same values same address reuse.

a  = [10]
b = [10]

print(id(a))
print(id(b))

#Ans : list is mutable can be change. 
# New address created for each new list.