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
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 3/4

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 4/4

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
