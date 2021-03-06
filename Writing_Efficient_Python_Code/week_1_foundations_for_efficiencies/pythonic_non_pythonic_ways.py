#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## A taste of things to come

# In this exercise, you'll explore both the Non-Pythonic and Pythonic ways of looping over a list. 

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# Suppose you wanted to collect the names in the above list that have six letters or more. In other programming languages, the typical approach is to create an index variable (i), 
# use i to iterate over the list, and use an if statement to collect the names with six letters or more:

i = 0
new_list= []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
print( new_list)

#['Kramer', 'Elaine', 'George', 'Newman']

# Let's explore some more Pythonic ways of doing this.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## A more Pythonic approach would loop over the contents of names, rather than using an index variable.

# Print the list created by looping over the contents of names
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print(better_list)

#['Kramer', 'Elaine', 'George', 'Newman']

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## The best Pythonic way of doing this is by using list comprehension

# Print the list created by using list comprehension
best_list = [name for name in names if len(name) >= 6]
print(best_list )

#['Kramer', 'Elaine', 'George', 'Newman']
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Remember, Pythonic code == efficient code

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
