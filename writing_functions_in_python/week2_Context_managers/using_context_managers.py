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
# The speed of cats

# You're working on a new web service that processes Instagram feeds to identify which pictures contain cats (don't ask why -- it's the internet). 
# The code that processes the data is slower than you would like it to be, so you are working on tuning it up to run faster. Given an image, image, 
# you have two functions that can process it:

    # process_with_numpy(image)
    # process_with_pytorch(image)

# Your colleague wrote a context manager, timer(), that will print out how long the code inside the context block takes to run. 
# She is suggesting you use it to see which of the two options is faster. Time each function to determine which one to use in your web service.


# Use the timer() context manager to time how long process_with_numpy(image) takes to run.
# Use the timer() context manager to time how long process_with_pytorch(image) takes to run.

image = get_image_from_instagram()

# Time how long process_with_numpy(image) takes to run
with timer():
  print('Numpy version')
  process_with_numpy(image)

# Time how long process_with_pytorch(image) takes to run
with timer():
  print('Pytorch version')
  process_with_pytorch(image)
  
# Numpy version
# Processing..........done!
# Elapsed: 1.53 seconds
# Pytorch version
# Processing..........done!
# Elapsed: 0.33 seconds
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
