# 14.02.2021

# Exercise
# num1 = input("Type the 1st number: ")
# num2 = input("Type the 2nd number: ")
# num3 = input("Type the 3d number: ")
# num4 = input("Type the 4nd number: ")
#
# if num1 > num2 and num3 > num4:
#     print("The first requirment is fullfilled!")
# elif num1 < num3 and num2 < num2 < num4:
#     print("The sedond requirment is fullfilled")
# elif num1 == num4 or num2  >= num4:
#     print("The third requirment is fullfilled")
# elif num1 <= num4 and num2 == num3:
#     print("The fourth requirment is fullfilled")
# else:
#     print("No requirment is fullfilled!")

# Lists
# weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday",  "Friday", "Saturday", "Sunday"]
# print(weekdays)
# print(weekdays[3])
# print(weekdays[3]  + " " +  " " + weekdays[2])

# Exercise
'''
Write a program that creates at least four different lists
'''
# StringList = ["string1", "string2", "string3"]
# print(StringList)
# NumberList = [3,  5,  7]
# print(NumberList)
# MixedList = [3, "string1", 5, "string2", True]
# print(MixedList)
# MixedList = StringList + NumberList + MixedList
# print(MixedList)


# Range function
# RangeList1 = list(range(4))
# print(RangeList1)
# RangeList2 = list(range(4,9))
# print(RangeList2)
# RangeList3 = list(range(4,10,2))
# print(RangeList3)

# Exersice
# number1 = int(input("Type a length number: "))
# List1 = list(range(number1))
# print(List1)
# print(len(List1))
#
# number2 = int(input("Type a length number: "))
# List2 = list(range(1, number2))
# print(List2)
# print(len(List2))
#
# number3 = int(input("Type a length number: "))
# List3 = list(range(2, number3, 2))
# print(List3)
# print(len(List3))

# Exeercise
# number = int(input("Type a number : "))
# List1 = list(range(1, number))
# print(List1)
# number = int(input("Type a number : "))
# List2 = list(range(2, number, 2))
# print(List2)
# number = int(input("Type a number : "))
# List3 = list(range(3, number, 3))
# print(List3)

# List functions
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
