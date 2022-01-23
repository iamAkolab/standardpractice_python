#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Code profiling for memory usage

# Quick and dirty approach

# One basic approach for inspecting memory consumption is using Python's built-in module sys. 
import sys

# This module contains system specific functions and contains one nice method, getsizeof(), that returns the size of an object in bytes. 

num_list = [*range(1000)]
sys.getsizeof(num_list)
# 9112

# The sys-dot-getsizeof is a quick and dirty way to see the size of an object. But, this only gives us the size of an individual object. 


#  What if we wanted to inspect the line-by-line memory footprint of our code? We'll have to use a code profiler! 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Code Profiling: Memory

# Detailed stats on memeory consumption
# Line-by-line analyses
# Package used: memory_profiler

$ pip install memory_profiler

# using memory_profiler package
%load_ext memory_profiler
%mprun -f cconvert_units convert_units(heroes, hts, wts)

# One drawback to using %mprun is that any function profiled for memory consumption must be defined in a file and imported. 
# %mprun can only be used on functions defined in physical files, and not in the IPython session. 

# %mprun output is similar to %lprun output. Here, we see a line-by-line description of the memory consumption for the function in question.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Pop quiz: steps for using %mprun

# Suppose you have a list of superheroes (named heroes) along with each hero's height (in centimeters) and weight (in kilograms) loaded as NumPy arrays (named hts and wts, 
# respectively). You also have a convert_units() function saved in a file titled hero_funcs.py.

# What are the necessary steps you need to take in order to profile the convert_units() function acting on your superheroes data if you'd like to see the line-by-line 
# memory consumption of convert_units()?

# Step 1: Use the command from hero_funcs import convert_units to load the function you'd like to profile.
# Step 2: Use %load_ext memory_profiler to load the memory_profiler within your IPython session.
# Step 3: Use %mprun -f convert_units convert_units(heroes, hts, wts) to get line-by-line memory allocations.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
