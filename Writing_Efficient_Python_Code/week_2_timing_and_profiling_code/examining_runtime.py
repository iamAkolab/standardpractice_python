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

# timing with %timeit
%timeit rand_nums = np.random.num(1000)
# 8.61 us +/- 69.1 ns per loop (mean +/- std. dev. 7 runs, 100000 loops each)


# specifying number of runs/loops
# setting the number of runs (-r)  and / or loops (-n)

# Set number of runs to 2 (-r)
# Set number of loops to 10
%timeit -r2 -n10 rand_nums = np.random.num(1000)
# 16.9 us +/- 5.14 ns per loop (mean +/- std. dev. 2 runs, 10 loops each)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
