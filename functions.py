# Example
def sumup(a,b): # this first line is function's signature
    sum = a + b
    return sum
cal_sum = sumup(2,3)
print(cal_sum)

def sumup(a,b):
    sum = a + b
    #return sum # retuns None afrer calling whithou return
cal_sum = sumup(2,3)
print(cal_sum)

# Exercise 28 (a)
# Write a function that sums up 2 numbers
def add_func (a,b):
    addition = a+b
    return addition
print(add_func(1,1))
print(add_func(2,2))
print(add_func(3,3))

# Exercise 28 (b)
# Write a function that subtract the 2d number from the 1st number
def subt_func (a,b):
    subtraction = a-b
    return subtraction
print(subt_func(3,1))
print(subt_func(3,2))
print(subt_func(3,3))

# Exercise 28 (c)
# Write a function that multiplies 2 numbers
def mult_func (a,b,c):
    multiplication = a*b*c
    return multiplication
print(mult_func(1,2,2))
print(mult_func(3,2,1))
print(mult_func(3,3,3))

# Exercise 28 (d)
# Write a function that divide the 1st number over the 2nd number
def div_func (a,b):
    division = a/b
    return division

print(div_func(1,2))
print(div_func(3,2))
print(div_func(3,3))

# Exercise 29
# Write a program that contatis 2 different functions
# 1. Takes list as an argument and returns the sum of all elements in the list,
# calculated by a loop

def get_sum_list (mylist):
    sum = 0
    for i in range(0,len(mylist)):
                    sum += mylist[i]
    #print(sum)
    return sum

get_sum_list([1,2,3,5])

# 2. Takes list as an argument and returns a reviersed list, using a loop
def get_reverse_list (mylist):
    new_list = []
    for i in mylist[::-1]:
        new_list.append(i)
    return new_list

get_reverse_list([1,2,3,4])


# Exercise 30 (a)
# Function for finding a maximum value in the nested list
def find_max_value (nested_list):
    max_num = 0

    for i in range(0, len(nested_list)):
        for j in range(0, len(nested_list[i])):
            if nested_list[i][j] > max_num:
                max_num = nested_list[i][j]
    print(f"That is a maximum number in the nested list provide:")
    return max_num
find_max_value([[1,2,3,444,7777],[3,99,40],[50,44,12,100]])

# Exercise 30 (b)
# Function for calculating a sum of all values in the nested list
def sum_of_elems (nested_list):
    sum_of_elem = 0
    for i in range(0, len(nested_list)):
        for j in range(0, len(nested_list[i])):
            sum_of_elem += nested_list[i][j]
    print(f"That is a sum of all elements in the nested list provide:")
    return sum_of_elem

sum_of_elems([[1,1,1,1],[1,1,1],[1,1,1,100]])

# Exercise 30 (c)
import random

# Function for calculating a sum of all values in the nested list
def mult_of_nested_lists (nested_list1, nested_list2, nested_list3):
    for i in range(0,len(nested_list1)):
        for j in range(0, len(nested_list2)):
            mult = nested_list1[i][j] * nested_list2[i][j]
            nested_list3[i][j]= mult
    return nested_list3


a = [list(random.sample(range(10,100),5)), list(random.sample(range(10,100),5)), list(random.sample(range(10,100),5))]
print(a)
b = [list(random.sample(range(10,100),5)), list(random.sample(range(10,100),5)), list(random.sample(range(10,100),5))]
print(b)
c = [list(random.sample(range(10,100),5)), list(random.sample(range(10,100),5)), list(random.sample(range(10,100),5))]
print(c)
mult_of_nested_lists(a, b, c)
