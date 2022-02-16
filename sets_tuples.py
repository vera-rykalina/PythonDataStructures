# Tuples
'''
- notation: mytuple = (1,2,3)
- very similar to lists but tuples are IMMUTABLE
- ordered (order cannot be changed)
- indexed: mytuple[1] -> to get an element at the index 1
- cannot be initiated as follows: my_tuple = ()
'''

mytuple = (1, 2, 3)
print(mytuple)
my_tuple = () # this will initialize an empty tuple
print(type(my_tuple)) # <class 'tuple'>
print(len(my_tuple)) # length of empty tuple is 0

# Exercise
# Create 4 tuples and print the item in each of them based on the user's input
len1 = int(input("Set length 1: "))
len2 = int(input("Set length 2: "))
len3 = int(input("Set length 3: "))
len4 = int(input("Set length 4: "))

mytuple1 = tuple(range(len1-1))
print(mytuple1)
mytuple2 = tuple(range(len2-1))
print(mytuple2)
mytuple3 = tuple(range(len3-1))
print(mytuple3)
mytuple4 = tuple(range(len4-1))
print(mytuple4)


index1 = int(input("What index to print for tuple 1? "))
print(f"That is your output: {mytuple1[index1-1]}")

index2 = int(input("What index to print for tuple 2? "))
print(f"That is your output: {mytuple1[index2-1]}")

index3 = int(input("What idex to print for tuple 3? "))
print(f"That is your output: {mytuple1[index3-1]}")

index4 = int(input("What idex to print for tuple 4? "))
print(f"That is your output: {mytuple1[index4-1]}")

# Sets
'''
- unordered collections of unique elements
- unchangeable (an item cannot be replaced by another intem: can be either added or removed although)
- unindexed (myset[1] - won't work!)
- cannot be initiated as follows: myset = {} - this will generates an empty dictionary
- myset.pop()  -> this will remove the first element in the set
- myset.add("new element") -> this will add a new element at the end of the set
'''
myset1 = {1, 2, 3}
print(myset1)
myset2 = {1,2,2,3,1}
print(myset2)
myset2.add(5)
print(myset2)
print("This is set 3")
myset3 = set(range(5))
print(myset3)
mylist = {1,2,3,4,4}
print(list(mylist)) # excludes repeats from ist

# Exercise
# Create 4 sets and add an item or remove an item based on the user's input
len1 = int(input("Set length 1: "))
len2 = int(input("Set length 2: "))
len3 = int(input("Set length 3: "))
len4 = int(input("Set length 4: "))

myset1 = set(range(len1-1))
print(myset1)
myset2 = set(range(len2-1))
print(myset2)
myset3 = set(range(len3-1))
print(myset3)
myset4 = set(range(len4-1))
print(myset4)


index1 = int(input("What number to add ? "))
myset1.add(index1)
print(myset1)

index2 = int(input("What number to add ? "))
myset2.add(index2)
print(myset2)

index3 = int(input("What number to remove first? "))
myset3.remove(index3)
print(myset3)
index3_1 = int(input("What number to remove second? "))
myset3.remove(index3_1) # removes an item at index position
print(myset3)

print("Removing the first element")
myset3.pop() # removes the first item from a set
print(myset3)

index4 = int(input("What number to add ? "))
myset4.add(index4)
print(myset4)
