#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Scraping the NASDAQ

# Training deep neural nets is expensive! You might as well invest in NVIDIA stock since you're spending so much on GPUs. To pick the best time to invest, you are going to 
# collect and analyze some data on how their stock is doing. The context manager stock('NVDA') will connect to the NASDAQ and return an object that you can use to get the 
# latest price by calling its .price() method.

# You want to connect to stock('NVDA') and record 10 timesteps of price data by writing it to the file NVDA.txt.

# You will notice the use of an underscore when iterating over the for loop. If this is confusing to you, don't worry. It could easily be replaced with i, if we planned to 
# do something with it, like use it as an index. Since we won't be using it, we can use a dummy operator, _, which doesn't use any additional memory.

# Use the stock('NVDA') context manager and assign the result to nvda.
# Open a file for writing with open('NVDA.txt', 'w') and assign the file object to f_out so you can record the price over time.


# Use the "stock('NVDA')" context manager
# and assign the result to the variable "nvda"
with stock('NVDA') as nvda:
  # Open "NVDA.txt" for writing as f_out
  with open('NVDA.txt', 'w') as f_out:
    for _ in range(10):
      value = nvda.price()
      print('Logging ${:.2f} for NVDA'.format(value))
      f_out.write('{:.2f}\n'.format(value))
 

# Output
 """
 Opening stock ticker for NVDA
Logging $139.50 for NVDA
Logging $139.54 for NVDA
Logging $139.61 for NVDA
Logging $139.65 for NVDA
Logging $139.72 for NVDA
Logging $139.73 for NVDA
Logging $139.80 for NVDA
Logging $139.78 for NVDA
Logging $139.73 for NVDA
Logging $139.64 for NVDA
Closing stock ticker
 """"

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Changing the working directory

# You are using an open-source library that lets you train deep neural networks on your data. Unfortunately, during training, this library writes out checkpoint models 
# (i.e., models that have been trained on a portion of the data) to the current working directory. You find that behavior frustrating because you don't want to have to 
# launch the script from the directory where the models will be saved.

# You decide that one way to fix this is to write a context manager that changes the current working directory, lets you build your models, and then resets the working 
# directory to its original location. You'll want to be sure that any errors that occur during model training don't prevent you from resetting the working directory to its 
# original location.


 # Add a statement that lets you handle any errors that might occur inside the context.
 # Add a statement that ensures os.chdir(current_dir) will be called, whether there was an error or not.

def in_dir(directory):
  """Change current working directory to `directory`,
  allow the user to run some code, and change back.

  Args:
    directory (str): The path to a directory to work in.
  """
  current_dir = os.getcwd()
  os.chdir(directory)

  # Add code that lets you handle errors
  try:
    yield
  # Ensure the directory is reset,
  # whether there was an error or not
  finally:
    os.chdir(current_dir)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
