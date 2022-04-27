# 14.02.2022
# Intro to data structures in Pyhton (Lists)

# Exercise
num1 = input("Type the 1st number: ")
num2 = input("Type the 2nd number: ")
num3 = input("Type the 3d number: ")
num4 = input("Type the 4nd number: ")

if num1 > num2 and num3 > num4:
    print("The first requirment is fullfilled!")
elif num1 < num3 and num2 < num2 < num4:
    print("The sedond requirment is fullfilled")
elif num1 == num4 or num2  >= num4:
    print("The third requirment is fullfilled")
elif num1 <= num4 and num2 == num3:
    print("The fourth requirment is fullfilled")
else:
    print("No requirment is fullfilled!")

# Lists
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday",  "Friday", "Saturday", "Sunday"]
print(weekdays)
print(weekdays[3])
print(weekdays[3]  + " " +  " " + weekdays[2])

# Exercise
'''
Write a program that creates at least four different lists
'''
StringList = ["string1", "string2", "string3"]
print(StringList)
NumberList = [3,  5,  7]
print(NumberList)
MixedList = [3, "string1", 5, "string2", True]
print(MixedList)
MixedList = StringList + NumberList + MixedList
print(MixedList)


# Range() function
RangeList1 = list(range(4))
print(RangeList1)
RangeList2 = list(range(4,9))
print(RangeList2)
RangeList3 = list(range(4,10,2))
print(RangeList3)

# Exersice
number1 = int(input("Type a length number: "))
List1 = list(range(number1))
print(List1)
print(len(List1))

number2 = int(input("Type a length number: "))
List2 = list(range(1, number2))
print(List2)
print(len(List2))

number3 = int(input("Type a length number: "))
List3 = list(range(2, number3, 2))
print(List3)
print(len(List3))

# Exercise
number = int(input("Type a number : "))
List1 = list(range(1, number))
print(List1)
number = int(input("Type a number : "))
List2 = list(range(2, number, 2))
print(List2)
number = int(input("Type a number : "))
List3 = list(range(3, number, 3))
print(List3)

# List methods
import random
mylist =[1,3,10,5,2]
print(mylist)
mylist.sort()
print(mylist)

mylist.append(222)
print(mylist)
mylist.pop()
print(mylist)
mylist.reverse()
print(mylist)
random.shuffle(mylist)
print(mylist)

# Exercise
list1 = list(range(4))
list2 = list(range(8))
list3 = list(range(1,4))
list4 = list(range(4, 10, 2))
list5 = list(range(1,4))
list6 = ["That",  "is", "interesting!"]
list1.append(list3)
print(list1)
list2.append(list4)
print(list4)
list1.extend(list5)
print(list1)
list2.extend(list6)
print(list2)

# List slicing
myList = list(range(16))
print(myList)
myNewList = myList[2:5]
print(myNewList)

# Exercise
list1 = list(range(30))
list2 = list(range(10,50))

slice_number1 = int(input("Type number 1: "))
slice_number2 = int(input("Type number 2: "))
slice_number3 = int(input("Type number 3: "))
slice_number4 = int(input("Type number 4: "))

if slice_number1 > (len(list1)-1 and len(list2)-1) or slice_number2  > (len(list1)-1 and len(list2)-1) or slice_number3 >  (len(list1)-1 and len(list2)-1) or slice_number4  > (len(list1)-1 and len(list2)-1):
    print("Type a smaller number:")
    slice_number1 = int(input("Type number 1 again: "))
    slice_number2 = int(input("Type number 2 again: "))
    slice_number3 = int(input("Type number 3 again: "))
    slice_number4 = int(input("Type number 4 again: "))
    if slice_number1 > (len(list1)-1 and len(list2)-1) or slice_number2  > (len(list1)-1 and len(list2)-1) or slice_number3 >  (len(list1)-1 and len(list2)-1) or slice_number4  > (len(list1)-1 and len(list2)-1):
        print("It is still a big number!")
        new_list1 = list1[slice_number1: slice_number2]
        print(new_list1)
        new_list2 = list2[slice_number3: slice_number4]
        print(new_list2)

if slice_number1 < (len(list1)-1 and len(list2)-1) or slice_number2  < (len(list1)-1 and len(list2)-1) or slice_number3  <  (len(list1)-1 and len(list2)-1) or slice_number4  < (len(list1)-1 and len(list2)-1):
    new_list1 = list1[slice_number1: slice_number2]
    print(new_list1)
    new_list2 = list2[slice_number3: slice_number4]
    print(new_list2)

# Exercise
list_length = int(input("Choose a length of a list. Type a number: "))
userlist = list(range(list_length))
end = int(input("Type number 1: "))
start = int(input("Type number 2: "))
skip1 = int(input("Type number 3: "))
skip2 = int(input("Type number 4: "))
print(userlist)
list1 = userlist[:end]
print(list1)
list2 = userlist[start:]
print(list2)
list3 = userlist[::skip1]
print(list3)
list4 = userlist[::skip2]
print(list4)

# Removing items from a list
mylist = ["apple", "banana", "orange", "whisky", "strawberry"]
print(mylist.index("banana"))
print(mylist)
mylist.append("pear")
print(mylist)
mylist.remove("apple")
print(mylist)
mylist.pop(-2)
print(mylist)
mylist.remove(mylist[-2])
print(mylist)


# Exercise
fruits= ["apple", "banana", "orange", "peach", "grape"]
animals = ["cat", "bear", "pig", "dog", "tiger" ]
colors=["red", "blue", "yellow"]
print(fruits)
print(animals)
print(colors)
select_fruit = input("Select an item be removed from the list of fruits: ")
fruits.remove(select_fruit)
print(fruits)
print(f"No {select_fruit} anymore!")
select_animal = input("Select an item be removed from the list of animals: ")
animals.remove(select_animal)
print(animals)
print(f"You got rid of a poor {select_animal}!")
select_color = input("Select an item be removed from the list of colors: ")
colors.remove(select_color)
print(colors)
print(f"You did it! The color {select_color} is out!")


