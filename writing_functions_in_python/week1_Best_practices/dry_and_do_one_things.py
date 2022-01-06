#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Don't Repeat Yourself (DRY)
-- it is easy to accidently introduce 
-- if you want to change something you have to change it in multiple places
-- repeated code is a sign that you need to write function


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Do one thing
-- code becomes flexible
-- less complex and more easily understand
-- easier to test
-- simpler to debug
-- easier to update

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Repeating code and functions that do more than 1 thing are examples of code smells, which are indication that you may need to refactor
# Refactoring is the process of improving code by changing it at a time
# Martin Fowler Book, Refactoring
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Extract a function

# While you were developing a model to predict the likelihood of a student graduating from college, you wrote this bit of code to get the z-scores of students' yearly GPAs. 
# Now you're ready to turn it into a production-quality system, so you need to do something about the repetition. Writing a function to calculate the z-scores would improve 
# this code.

# Standardize the GPAs for each year
df['y1_z'] = (df.y1_gpa - df.y1_gpa.mean()) / df.y1_gpa.std()
df['y2_z'] = (df.y2_gpa - df.y2_gpa.mean()) / df.y2_gpa.std()
df['y3_z'] = (df.y3_gpa - df.y3_gpa.mean()) / df.y3_gpa.std()
df['y4_z'] = (df.y4_gpa - df.y4_gpa.mean()) / df.y4_gpa.std()

# Note: df is a pandas DataFrame where each row is a student with 4 columns of yearly student GPAs: y1_gpa, y2_gpa, y3_gpa, y4_gpa
# Finish the function so that it returns the z-scores of a column.
# Use the function to calculate the z-scores for each year (df['y1_z'], df['y2_z'], etc.) from the raw GPA scores (df.y1_gpa, df.y2_gpa, etc.).

def standardize(column):
  """Standardize the values in a column.

  Args:
    column (pandas Series): The data to standardize.

  Returns:
    pandas Series: the values as z-scores
  """
  # Finish the function so that it returns the z-scores
  z_score = (column - column.mean()) / column.std()
  return z_score

# Use the standardize() function to calculate the z-scores
df['y1_z'] = standardize(df.y1_gpa)
df['y2_z'] = standardize(df.y2_gpa)
df['y3_z'] = standardize(df.y3_gpa)
df['y4_z'] = standardize(df.y4_gpa)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Split up a function

# Another engineer on your team has written this function to calculate the mean and median of a sorted list. You want to show them how to split it into two simpler functions: 
# mean() and median()

def mean_and_median(values):
  """Get the mean and median of a sorted list of `values`

  Args:
    values (iterable of float): A list of numbers

  Returns:
    tuple (float, float): The mean and median
  """
  mean = sum(values) / len(values)
  midpoint = int(len(values) / 2)
  if len(values) % 2 == 0:
    median = (values[midpoint - 1] + values[midpoint]) / 2
  else:
    median = values[midpoint]

  return mean, median

# Write the mean() function
def mean(values):
  """Get the mean of a sorted list of values

  Args:
    values (iterable of float): A list of numbers

  Returns:
    float
  """
  # Write the mean() function
  mean = sum(values) / len(values)
  return mean


# Write the median() function.
def median(values):
  """Get the median of a sorted list of values

  Args:
    values (iterable of float): A list of numbers

  Returns:
    float
  """
  # Write the median() function
  midpoint = int(len(values) / 2)
  if len(values) % 2 == 0:
    median = (values[midpoint - 1] + values[midpoint]) / 2
  else:
    median = values[midpoint]
  return median
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

