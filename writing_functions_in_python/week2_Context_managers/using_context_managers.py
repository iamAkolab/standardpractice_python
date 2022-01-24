#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## What is a context manager

# A context manager is a type of function that sets up a context for your code to run in, runs your code, and then removes the context.

# A real world example

with open('my_file.txt') as my_file:
  text = my_file.read()
  length = len(text)
  
print('The file is {} characters long'.format(length))

# open() does three things:
  # sets up a context by opening a file
  # lets you run any code you want on that file

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
