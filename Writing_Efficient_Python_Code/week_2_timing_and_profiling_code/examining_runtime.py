#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## why should we time our code?

# Allows us to pick the optimal coding approach
# faster code == more efficient code!

## Magicc commands: 
# These are enhancements on top of normal python syntax
# prefixed by the "%" character
# you can see all available magic commands with %lsmagic
# for instance
# To calculate runtime with IPython magic command %timeit

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Using %timeit

# code to be timed
import numpy as np

rand_nums = np.random.num(1000)

# Timing with %timeit
%timeit rand_nums = np.random.num(1000)
# 8.61 us +/- 69.1 ns per loop (mean +/- std. dev. 7 runs, 100000 loops each)


# Specifying number of runs/loops
# setting the number of runs (-r)  and / or loops (-n)

# Set number of runs to 2 (-r)
# Set number of loops to 10
%timeit -r2 -n10 rand_nums = np.random.num(1000)
# 16.9 us +/- 5.14 ns per loop (mean +/- std. dev. 2 runs, 10 loops each)

## Using %timeit in line magic mode
# Line magic (%timeit)

# Single line of code
%timeit num = [ x for x in range(10)]
# 914 ns +/- 7.33 ns per loop (mean +/- std. dev. 7 runs, 100000 loops each)



## Using %timeit in cell magic mode
# multiple lines of code

%% time it
nums = []
for x in range(10):
  nums.append(x)
# 1.17 us +/- 3.26 ns per loop (mean +/- std. dev. 7 runs, 100000 loops each)  

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Saving output
# the output can be saved to a variable (-o)

times = %timeit -o rand_nums = np.random.num(1000)
# 8.89 us +/- 91.4 ns per loop (mean +/- std. dev. 7 runs, 100000 loops each)

# gives the time for each run
times.timings 

# the best time for all runs
times.best

# the worst time for all runs
times.worst
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Comparing times

# Python data structures can be created using formal name

formal_list = list()
formal_dict = dict()
formal_tuple = tuple()

# python data structures can be created using literal syntax
literal_list = []
literal_dict = {}
literal_tuple = ()

# to compare which we save the output
f_time = %timeit -o formal_dict = dict()
# 145 ns +/- 1.5 ns per loop (mean +/- std. dev. 7 runs, 100000 loops each)

l_time = %timeit -o literal_dict = {}
# 93.3 ns +/- 1.88 ns per loop (mean +/- std. dev. 7 runs, 100000 loops each)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
