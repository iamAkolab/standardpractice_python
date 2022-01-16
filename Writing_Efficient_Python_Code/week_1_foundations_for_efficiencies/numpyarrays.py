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

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
