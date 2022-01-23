
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##  Code Profiling

# Code Profiling is a technique used to describe how long, and how often, various parts of a program are executed.

# Detailed stats on frequency and duration of function calls
# Line-by-line analyses
# We'll focus on the line_profiler package to profile a function's runtime line by line

$ pip install line_profiler

# Example: Suppose we have a list of superheroes along with each hero's height (in cm) and weight (in kilogram) loaded as Numpy arrays
import numpy as np 

heroes = ['Batman', 'Superman', 'Wonder Woman']
hts = np.array([188.0, 191.0, 183.0])
wts = np.array([95.0, 101.0, 74.0])


# we have also created a function convert_units that converts the hero's height from centimeters to inches and weights from kilograms to pounds

def convert_units(heroes, heights, weights):
  
  new_hts = [ht * 0.39370 for ht in heights]
  new_hts = [wt * 2.20462 for wt in weights]
  
  hero_data = {}
  
  for i, hero in enumerate(heroes):
    hero_data[hero] = (new_hts[i], new_wts[i])
    
  return hero_data


convert_units(heroes, hts, wts)


# using line_profiler package 
%load_ext line_profiler

# magic command for line-by-line times
%lprun -f convert_units convert_units(heroes, hts, wts)
# - f indicates we want to profile a function, Next we specify the name of the function we'd like to porfile.
# finally we provide the exact function call we'd like to profile by including any arguments that are needed

# The output provides a nice table that summarizes the profiling statistics
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
