# 15.02.2014

'''
Contents:
lists (methods and functions)
multidimensional lists (creating and getting an element)
dictionaries

'''

# Lists
# Checking, if an item is within a list

# mylist1 = list(range(9)) # a list of integers
# print(mylist1)
# check1 = 4
# check2 = 12
# if check1 in mylist1:
#     print("This value is in the list")
# if check2 not in mylist1:
#     print("The value is not in the list")
#
# mylist2 = ["Hello", "world", "!"] # a list of strings
# if "Hello" in mylist2:
#     print("A word 'Hello' is in the list")

# Exercise
'''
- Write a program that genetares a list with contents of your choise
- Then let the user input at least 3 different things
- Check whether these inputs are parts of your list or not
- Print out an appropriate answer
'''

# colors = ["red",  "black", "blue", "white", "lilac" ]
# print(colors)
# color1 = input("Choose the first color and type it: ")
# color2 = input("Choose the second color and type it: ")
# color3 = input("Choose the third color and type it: ")
#
# if color1 in colors:
#     print(f"A color {color1} is within the list")
# else:
#     print(f"A color {color1} is not within the list")
# if color2 in colors:
#     print(f"A color{color2} is within the list")
# else:
#     print(f"A color {color2} is not within the list")
# if color3 in colors:
#     print(f"A color {color3} is within the list")
# else:
#     print(f"A color {color3} is not within the list")

# List method insert()
# Method insert() allows you to insert an item at a defined index position
# mylist3 = list(range(16))
# mylist3.insert(3, "INSERTION")
# print(mylist3)
# mylist3.insert(0, 10000)
# print(mylist3)


# Exercise
'''
- Write a program that generates 3 lists of different sizes and print them out
- Let the user choose where within these lists he wants to insert a number
- Do not forget to check whether the chosen index is a part of the list or not
'''
# numbers = list(range(16))
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
# odds = list(range(3, 99, 3))
#
# print(numbers)
# print(letters)
# print(odds)
#
# ins1 = int(input("Type an index: "))
# ins_num1 = int(input("Type a number to insert: "))
# ins2 = int(input("Type an index: "))
# ins_num2 = int(input("Type a letter to insert: "))
# ins3 = int(input("Type an index: "))
# ins_num3 = int(input("Type a number to insert: "))
#
# if ins1 < len(numbers)-1:
#     numbers.insert(ins1, ins_num1)
#     print(numbers)
# else:
#     print("Index is out of range for this list")
#
# if ins2 < len(letters)-1:
#     letters.insert(ins2, ins_num2)
#     print(letters)
# else:
#     print("Index is out of range for this list")
#
# if ins3 < len(odds)-1:
#     odds.insert(ins3, ins_num3)
#     print(odds)
# else:
#     print("Index is out of range for this list")

# Other list methods
# copy(),  sort(), index(), clear(), remove()
# functions: min(),  max()
# mylist_num = [2, 45, 6, 6, 9, 22, 199]
# mylist_num.sort()
# print(mylist_num)
# mylist_let = ["hello", "dog", "cat",  "bye", "BYe", "BYE"]
# mylist_let.sort()
# print(mylist_let)
#
# print(max(mylist_num))
# print(mylist_num.count(6))
# mylist_num.reverse()
# print(mylist_num)
# print(mylist_num.index(6))
# newlist_num = mylist_num.copy()
# print(newlist_num)
# newlist_num.clear()
# print(newlist_num) # reruns an empty list


# Multidimensional lists
# multi_dim_list = [[1,2,10],  [1,16,3], [1,2,3], [30,2,3]]
# print(multi_dim_list)
# print(multi_dim_list[0][2]) # retunrs "10"
#
# matrix = [list(range(3))] *3
# print(matrix)

# Exercise
'''
- Write a program that creates at least 3 different matrices with different sizes
- One of them should be quadratic
- One should have more columns than rows
- One should have more rows than columns
- Let the user input the dimentsions of the matrices
'''
# mat1 = [list(range(2))] *2
# print(mat1)
# row1 = int(input("Type a row number for the 1st matix: "))-1
# col1 = int(input("Type a colum number for the 1st matrix: "))-1
# print(mat1[row1][col1])
#
# mat2 = [list(range(5))] *3
# print(mat2)
# row2 = int(input("Type a row number for the 2nd matix: "))-1
# col2 = int(input("Type a colum number for the 2nd matrix: "))-1
# print(mat2[row2][col2])
#
#
# mat3 = [list(range(3))] *5
# print(mat2)
# row3 = int(input("Type a row number for the 3rd matix: "))-1
# col3 = int(input("Type a colum number for the 3rd matrix: "))-1
# print(mat3[row3][col3])

# mymatrix = [[1,2,3], [1,2,3], [1,2,3]]
# print(mymatrix)
# mymatrix[1].remove(mymatrix[1][1]) # removes "2" from the middle list
# print(mymatrix)
# mylist = [1,2,3]
# print(mylist)
# mylist.remove(mylist[1])
# print(mylist)


# Dictionaries
# mydic = {}
# mydic["k1"] = 12
# mydic["k2"] = 20
# mydic["k3"] = 55
# print(mydic)
# print(mydic.values())
# print(mydic.keys())
# print(type(mydic.keys()))
# print(list(mydic.keys())) # convert keys into a list
# print(mydic["k1"])
#
# if "k1" in mydic:
#     print(" k1 is available")

# Exercise
'''
- Write a program that generates a simple dictionary consisting of at least 3 pre-defined entries
- Ask the user for a new entry and add this new one to the dictionary afterwords
- Then ask the user for an entry that should be removed and remove the entry from the dictionary
- Print out the remaining dictionary
'''
# person = {"age": 32, "height": 170, "gender": "female"}
# counter = 0
# while counter < 3:
#     print(person)
#     new_key = input("Add a feature: ")
#     new_value = input(f"Add a value for the feature '{new_key}' : ")
#     person[new_key] = new_value
#     print(person)
#     rem_key = input("Add a feature to remove: ")
#     person.pop(rem_key)
#     print(person)
#     counter += 1

# Exercise
'''
- Create a dictionary with at least ten entries
- Let the user search the dictionary for a specific entry
- If the entry is already present, ask the user for an update the entry; if the entry does not exist, add it to the dictionary
 - Run this option at least 3 times during one call of the program
 - Print out th eoriginal dictionary and the modified one at the end
'''

person = {"age": 32, "height": 170, "gender": "female",  "mood": "good",  "profession": "biologist", "salary": 70000, "smoking": False, "children": 0, "weight": 65,  "city": "Berlin"}
# print(len(person)) # checks on length of the dictionary

counter = 0
while counter <= 3:

    new_key = input("What feature are you looking for? ")
    if new_key in person:
        print("This entry is already within the collection of features")
    else:
        new_dic=person.copy()
        new_value = input(f"Add a value for the feature '{new_key}' : ")
        new_dic[new_key] = new_value
        print(person)
        print(new_dic)
        counter += 1
