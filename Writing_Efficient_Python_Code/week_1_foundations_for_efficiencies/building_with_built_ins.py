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
## Built-in function: enumerate()

letters = ['a', 'b', 'c', 'd']

indexed_letters = enumerate(letters)

indexed_letters_list =  list(indexed_letters)
print(indexed_letters_list)

# [(0, 'a'), (1, 'b') , (2, 'c'), (3, 'd')]

# indexed_letters = enumerate(letters, start = 5)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Built-in function: map()

nums = [1.5, 2.3, 3.4, 4.6,5.0]

rnd_nums = map(round, nums)

print(list(rnd_nums))
# [2,3,4,5,5]

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##
