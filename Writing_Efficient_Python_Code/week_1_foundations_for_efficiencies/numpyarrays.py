#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## NUMPY ARRAYS

# Numpy is the fundamental package for scientific computing. Numpy arrays are homogeneous, they must contain element of the same type

import numpy as np

nums_np  = np.array(range(5))
# array([1,2,3,4])

nums_np.dtype
# dtype('int64')

# NumPY array support broadcasting, performing multiplications on all the elements of the array
# Basic indexing for 2-D arrays is simplier
# Supports Boolean Indexing
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Practice with NumPy arrays

# Print the second row of nums.
print(nums[1,:])
# [ 6  7  8  9 10]


# Print the items of nums that are greater than six.
print(nums[nums > 6])
#  [ 7  8  9 10]

# Create nums_dbl that doubles each number in nums.
nums_dbl = nums * 2
print(nums_dbl)
# [[ 2  4  6  8 10]
#  [12 14 16 18 20]]

 
# Replace the third column in nums with a new column that adds 1 to each item in the original column.
nums[:,2] = nums[:,2] + 1
print(nums)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]   
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Bringing it all together: Festivus!

# Use range() to create a list of arrival times (10 through 50 incremented by 10). Create the list arrival_times by unpacking the range object.
arrival_times = [*range(10,60,10)]
print(arrival_times)
# [10, 20, 30, 40, 50]


# You realize your clock is three minutes fast. Convert the arrival_times list into a numpy array (called arrival_times_np) and 
# use NumPy broadcasting to subtract three minutes from each arrival time.

# Create a list of arrival times
arrival_times = [*range(10,60,10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

print(new_times)
# [ 7 17 27 37 47]


# Use list comprehension with enumerate() to pair each guest in the names list to their updated arrival time in the new_times array. 
# You'll need to use the index variable created from using enumerate() on new_times to index the names list.

# Create a list of arrival times
arrival_times = [*range(10,60,10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i],time) for i,time in enumerate(new_times)]

print(guest_arrivals)
# [('Jerry', 7), ('Kramer', 17), ('Elaine', 27), ('George', 37), ('Newman', 47)]



# A function named welcome_guest() has been pre-loaded into your session. Use map() to apply this function to each element of the guest_arrivals list 
# and save it as the variable welcome_map

# Create a list of arrival times
arrival_times = [*range(10,60,10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i],time) for i,time in enumerate(new_times)]

# Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(*guest_welcomes, sep='\n')

# Welcome to Festivus Jerry... You're 7 min late.
# Welcome to Festivus Kramer... You're 17 min late.
# Welcome to Festivus Elaine... You're 27 min late.
# Welcome to Festivus George... You're 37 min late.
# Welcome to Festivus Newman... You're 47 min late.
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
