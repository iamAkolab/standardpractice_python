#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##  Bringing it all together: Star Wars profiling

# A list of 480 superheroes has been loaded into your session (called heroes) as well as a list of each hero's corresponding publisher (called publishers).
# You'd like to filter the heroes list based on a hero's specific publisher, but are unsure which of the below functions is more efficient. 

def get_publisher_heroes(heroes, publishers, desired_publisher):

    desired_heroes = []

    for i,pub in enumerate(publishers):
        if pub == desired_publisher:
            desired_heroes.append(heroes[i])

    return desired_heroes
  
def get_publisher_heroes_np(heroes, publishers, desired_publisher):

    heroes_np = np.array(heroes)
    pubs_np = np.array(publishers)

    desired_heroes = heroes_np[pubs_np == desired_publisher]

    return desired_heroes
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 1/4

# Use the get_publisher_heroes() function and the get_publisher_heroes_np() function to collect heroes from the Star Wars universe. 
# The desired_publisher for Star Wars is 'George Lucas'

# Use get_publisher_heroes() to gather Star Wars heroes
star_wars_heroes = get_publisher_heroes(heroes, publishers, 'George Lucas')

print(star_wars_heroes)
print(type(star_wars_heroes))

# Use get_publisher_heroes_np() to gather Star Wars heroes
star_wars_heroes_np = get_publisher_heroes_np(heroes, publishers, 'George Lucas')

print(star_wars_heroes_np)
print(type(star_wars_heroes_np))

# ['Darth Vader', 'Han Solo', 'Luke Skywalker', 'Yoda']
# <class 'list'>

# ['Darth Vader' 'Han Solo' 'Luke Skywalker' 'Yoda']
# <class 'numpy.ndarray'>
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 2/4

# Within your IPython console, load the line_profiler and use %lprun to profile the two functions for line-by-line runtime. When using %lprun, use each function to 
# gather the Star Wars heroes as you did in the previous step. After you've finished profiling, answer the following question:

%load_ext line_profiler 

%lprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, 'George Lucas')
'''
Timer unit: 1e-06 s

Total time: 0.000358 s
File: <ipython-input-1-5a6bc05c1c55>
Function: get_publisher_heroes at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def get_publisher_heroes(heroes, publishers, desired_publisher):
     2                                           
     3         1          3.0      3.0      0.8      desired_heroes = []
     4                                           
     5       481        177.0      0.4     49.4      for i,pub in enumerate(publishers):
     6       480        165.0      0.3     46.1          if pub == desired_publisher:
     7         4         13.0      3.2      3.6              desired_heroes.append(heroes[i])
     8                                           
     9         1          0.0      0.0      0.0      return desired_heroes
     
 '''

%lprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes, publishers, 'George Lucas')
'''
Timer unit: 1e-06 s

Total time: 0.000214 s
File: <ipython-input-1-5a6bc05c1c55>
Function: get_publisher_heroes_np at line 12

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    12                                           def get_publisher_heroes_np(heroes, publishers, desired_publisher):
    13                                           
    14         1        146.0    146.0     68.2      heroes_np = np.array(heroes)
    15         1         47.0     47.0     22.0      pubs_np = np.array(publishers)
    16                                           
    17         1         20.0     20.0      9.3      desired_heroes = heroes_np[pubs_np == desired_publisher]
    18                                           
    19         1          1.0      1.0      0.5      return desired_heroes

'''

#### Answer : get_publisher_heroes_np is faster
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 3/4

# Within your IPython console, load the memory_profiler and use %mprun to profile the two functions for line-by-line memory consumption.

# The get_publisher_heroes() function and get_publisher_heroes_np() function have been saved within a file titled hero_funcs.py (i.e., you can import both functions from 
# hero_funcs). When using %mprun, use each function to gather the Star Wars heroes as you did in the previous step. 

# After you've finished profiling, answer the following question: Which function uses the least amount of memory?

%load_ext line_profiler
from hero_funcs import get_publisher_heroes

%mprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, 'George Lucas')


%load_ext line_profiler
from hero_funcs import get_publisher_heroes_np

%mprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes, publishers, 'George Lucas')


# Answer: Both functions have the same memory consumption.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 4/4

# Based on your runtime profiling and memory allocation profiling, which function would you choose to gather Star Wars heroes?


# Answer: I would use get_publisher_heroes_np()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
