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
# Any time you use a context manager, it will look like this. 

with <context-manager>(<args>):
  # Run your code
  # This code is running "inside the context"
  
# This code runs after the context is removed

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  The number of cats

# You are working on a natural language processing project to determine what makes great writers so great. Your current hypothesis is that great writers talk about cats a lot. 
# To prove it, you want to count the number of times the word "cat" appears in "Alice's Adventures in Wonderland" by Lewis Carroll. You have already downloaded a text file, 
# alice.txt, with the entire contents of this great book.

# Use the open() context manager to open alice.txt and assign the file to the file variable

# Open "alice.txt" and assign the file to "file"
with open('alice.txt') as file:
  text = file.read()

n = 0
for word in text.split():
  if word.lower() in ['cat', 'cats']:
    n += 1

print('Lewis Carroll uses the word "cat" {} times'.format(n))
# Lewis Carroll uses the word "cat" 24 times
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
