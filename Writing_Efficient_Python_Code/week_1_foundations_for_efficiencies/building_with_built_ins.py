#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Building with built-ins
# This is referred to as the Python Standard Library. Part of every standard python

# Built-in types
# list, tuple, set, dict and others

# Built-in functions
# print(), len(), range(), round(), enumerate(), map(), zip() and others

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Built-in function: range()

# Using range with a step value

evens_nums = range(2, 11, 2)

even_nums_list = list(even_nums)
print(even_nums_list)

# [ 2 , 4, 8, 10]

# range is not inclusive
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## range() Exercise
# In this exercise, you will practice using Python's built-in function range(). Remember that you can use range() in a few different ways:

# 1) Create a sequence of numbers from 0 to a stop value (which is exclusive). This is useful when you want to create a simple sequence of numbers starting at zero:

range(stop)

# Example
list(range(11))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2) Create a sequence of numbers from a start value to a stop value (which is exclusive) with a step size. This is useful when you want to create a sequence of numbers 
# that increments by some value other than one. For example, a list of even numbers:

range(start, stop, step)

# Example
list(range(2,11,2))
# [2, 4, 6, 8, 10]

#############################################################################################
# Create a range object that starts at zero and ends at five. Only use a stop argument.
# Create a range object that goes from 0 to 5
nums = range(6)
print(type(nums))
# <class 'range'>

# Convert the nums variable into a list called nums_list.
# Convert nums to a list
nums_list = list(nums)
print(nums_list)
# [0, 1, 2, 3, 4, 5]

# Create a new list called nums_list2 that starts at one, ends at eleven, and increments by two by unpacking a range object using the star character (*).
# Create a new list of odd numbers from 1 to 11 by unpacking a range object
nums_list2 = [*range(1,12,2)]
print(nums_list2)
# [1, 3, 5, 7, 9, 11]
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Built-in function: enumerate()

letters = ['a', 'b', 'c', 'd']

indexed_letters = enumerate(letters)

indexed_letters_list =  list(indexed_letters)
print(indexed_letters_list)

# [(0, 'a'), (1, 'b') , (2, 'c'), (3, 'd')]

# indexed_letters = enumerate(letters, start = 5)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Built-in practice: enumerate()

# In this exercise, you'll practice using Python's built-in function enumerate(). This function is useful for obtaining an indexed list. For example, suppose you had a list of 
# people that arrived at a party you are hosting. The list is ordered by arrival (Jerry was the first to arrive, followed by Kramer, etc.):

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# If you wanted to attach an index representing a person's arrival order, you could use the following for loop:

indexed_names = []
for i in range(len(names)):
    index_name = (i, names[i])
    indexed_names.append(index_name)

[(0,'Jerry'),(1,'Kramer'),(2,'Elaine'),(3,'George'),(4,'Newman')]

# But, that's not the most efficient solution. Let's explore how to use enumerate() to make this more efficient.


#############################################################################################
# Instead of using for i in range(len(names)), update the for loop to use i as the index variable and name as the iterator variable and use enumerate().

# Rewrite the for loop to use enumerate
indexed_names = []
for i,name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(indexed_names)
# [(0, 'Jerry'), (1, 'Kramer'), (2, 'Elaine'), (3, 'George'), (4, 'Newman')]


# Rewrite the previous for loop using enumerate() and list comprehension to create a new list, indexed_names_comp.
indexed_names_comp = [(i,name) for i,name in enumerate(names)]
print(indexed_names_comp)
# [(0, 'Jerry'), (1, 'Kramer'), (2, 'Elaine'), (3, 'George'), (4, 'Newman')]

# Create another list (indexed_names_unpack) by using the star character (*) to unpack the enumerate object created from using enumerate() on names. 
# This time, start the index for enumerate() at one instead of zero.

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, 1)]
print(indexed_names_unpack)
# [(0, 'Jerry'), (1, 'Kramer'), (2, 'Elaine'), (3, 'George'), (4, 'Newman')]
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Built-in function: map()

nums = [1.5, 2.3, 3.4, 4.6,5.0]

rnd_nums = map(round, nums)

print(list(rnd_nums))
# [2,3,4,5,5]

# map() with lambda(anonymous function)
nums = [ 1, 2, 3,4 ,5]

sqrd_nums = map(lambda x:x ** 2, nums)

print(list(sqrd_nums)
      
 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Built-in practice: map()

# In this exercise, you'll practice using Python's built-in map() function to apply a function to every element of an object. Let's look at a list of party guests:

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# Suppose you wanted to create a new list (called names_uppercase) that converted all the letters in each name to uppercase. you could accomplish this with the below for loop:

names_uppercase = []

for name in names:
  names_uppercase.append(name.upper())

['JERRY', 'KRAMER', 'ELAINE', 'GEORGE', 'NEWMAN']

# Let's explore using the map() function to do this more efficiently in one line of code.
      
#############################################################################################
# Use map() and the method str.upper() to convert each name in the list names to uppercase. Save this to the variable names_map.
# Use map to apply str.upper to each element in names
names_map  = map(str.upper, names)


# Print the type of the names_map
print(list(names_map))
# [<map object at 0x7fd2865a88d0>] 
      
 
# Unpack the contents of names_map into a list called names_uppercase using the star character (*).
names_uppercase = [names_map] 
 
# Print names_uppercase and observe its contents.
print(names_uppercase)
# ['JERRY', 'KRAMER', 'ELAINE', 'GEORGE', 'NEWMAN']
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
