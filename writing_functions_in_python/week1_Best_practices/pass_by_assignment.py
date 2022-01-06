#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Immutable
# int float bool string bytes tuple frozenset None

## Mutable
# list dict set bytearray objects functions everything else

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Mutable default arguments are dangerious

def foo(var =[]):
  var.append(!)
  return var

foo()
# [1]

foo()
# [1, 1]

# better way is

def foo(var = None):
  if var is None:
    var = []
  var.append(1)
  return var

foo()
# [1]

foo()
# [1]
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Mutable or immutable?

# The following function adds a mapping between a string and the lowercase version of that string to a dictionary. What do you expect the values of d and s to be after the 
# function is called?

def store_lower(_dict, _string):
  """Add a mapping between `_string` and a lowercased version of `_string` to `_dict`

  Args:
    _dict (dict): The dictionary to update.
    _string (str): The string to add.
  """
  orig_string = _string
  _string = _string.lower()
  _dict[orig_string] = _string

d = {}
s = 'Hello'

store_lower(d, s)

# ANSWER
# d = {'Hello': 'hello'}, s = 'Hello'
# Correct! Dictionaries are mutable objects in Python, so the function can directly change it in the _dict[_orig_string] = _string statement. 
# Strings, on the other hand, are immutable. When the function creates the lowercase version, it has to assign it to the _string variable. 
# This disconnects what happens to _string from the external s variable.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Best practice for default arguments

# One of your co-workers (who obviously didn't take this course) has written this function for adding a column to a pandas DataFrame. Unfortunately, they used a mutable variable
# as a default argument value! Please show them a better way to do this so that they don't get unexpected behavior.

def add_column(values, df=pandas.DataFrame()):
  """Add a column of `values` to a DataFrame `df`.
  The column will be named "col_<n>" where "n" is
  the numerical index of the column.

  Args:
    values (iterable): The values of the new column
    df (DataFrame, optional): The DataFrame to update.
      If no DataFrame is passed, one is created by default.

  Returns:
    DataFrame
  """
  df['col_{}'.format(len(df.columns))] = values
  return df

# Change the default value of df to an immutable value to follow best practices.
# Update the code of the function so that a new DataFrame is created if the caller didn't pass one.

# Use an immutable variable for the default argument
def better_add_column(values, df=None):
  """Add a column of `values` to a DataFrame `df`.
  The column will be named "col_<n>" where "n" is
  the numerical index of the column.

  Args:
    values (iterable): The values of the new column
    df (DataFrame, optional): The DataFrame to update.
      If no DataFrame is passed, one is created by default.

  Returns:
    DataFrame
  """
  # Update the function to create a default DataFrame
  if df is None:
    df = pandas.DataFrame()
  df['col_{}'.format(len(df.columns))] = values
  return df
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
