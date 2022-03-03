#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
## How to create a context manager

# There are two ways to define a context manager in Python: 
# by using a class that has special __enter__() and __exit__() methods or 
# by decorating a certain kind of function. 


@contextlib.contextmanager
def my_context():
  # Add any set up you need
  yield
  # add any teardown code you need

# There are five parts to creating a context manager. 
# First, you need to define a function. 
# Next, you can add any setup code your context needs. This is not required though. 
# Third, you must use the "yield" keyword to signal to Python that this is a special kind of function. 
# After the "yield" statement, you can add any teardown code that you need to clean up the context.
# Finally, you must decorate the function with the "contextmanager" decorator from the "contextlib" module.

# For now, the important thing to know is that you write the "at" symbol, followed by "contextlib.contextmanager" on the line immediately above your context manager function. 

# The "yield" keyword may also be new to you. When you write this word, it means that you are going to return a value, but you expect to finish the rest of the function at some
# point in the future. The value that your context manager yields can be assigned to a variable in the "with" statement by adding "as <variable name>". Here, we've assigned the 
# value 42 that my_context() yields to the variable "foo". 


@contextlib.contextmanager
def my_context():
  print('hello')
  yield 42
  print('goodbye')
  
with my_context() as foo:
  print('foo is {}'.format(foo))

# hello
# foo is 42
# goodbye

# By running this code, you can see that after the context block is done executing, the rest of the my_context() function gets run, printing "goodbye". Some of you may recognize 
# the "yield" keyword as a thing that gets used when creating generators. In fact, a context manager function is technically a generator that yields a single value

# The ability for a function to yield control and know that it will get to finish running later is what makes context managers so useful. 

@contextlib.contextmanager
def database(url):
  
  # set up database connection
  db = postgres.connect(url)
  
  yield db
  
  # tear down database connection
  db.disconnect()
  
url = 'https:/datacamp.com/data'
with database(url) as my_db:
  course_list = my_db.execute('SELECT * FROM course')

# This context manager is an example of code that accesses a database. Like most context managers, it has some setup code that runs before the function yields. This context manager uses that setup code to connect 
# to the database. 


# Setup and teardown

# Most context managers also have some teardown or cleanup code when they get control back after yielding. This one uses the teardown section to disconnect from the database.

# This setup/teardown behavior allows a context manager to hide things like connecting and disconnecting from a database so that a programmer using the context manager can just
# perform operations on the database without worrying about the underlying details. 

# The database() context manager that we've been looking at yields a specific value - the database connection - that can be used in the context block. Some context managers 
# don't yield an explicit value. in_dir() is a context manager that changes the current working directory to a specific path and then changes it back after the context block is
# done. It does not need to return anything with its "yield" statement. 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# The timer() context manager

# A colleague of yours is working on a web service that processes Instagram photos. Customers are complaining that the service takes too long to identify whether or not an 
# image has a cat in it, so your colleague has come to you for help. You decide to write a context manager that they can use to time how long their functions take to run.

#  Add a decorator from the contextlib module to the timer() function that will make it act like a context manager.
#  Send control from the timer() function to the context block.

# Add a decorator that will make timer() a context manager
@contextlib.contextmanager
def timer():
  """Time the execution of a context block.

  Yields:
    None
  """
  start = time.time()
  # Send control back to the context block
  yield time
  end = time.time()
  print('Elapsed: {:.2f}s'.format(end - start))

with timer():
  print('This should take approximately 0.25 seconds')
  time.sleep(0.25)
  
# This should take approximately 0.25 seconds
# Elapsed: 0.25s
  
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
## A read-only open() context manager

# You have a bunch of data files for your next deep learning project that took you months to collect and clean. It would be terrible if you accidentally overwrote one of
# those files when trying to read it in for training, so you decide to create a read-only version of the open() context manager to use in your project.

# The regular open() context manager:

    # takes a filename and a mode ('r' for read, 'w' for write, or 'a' for append)
    # opens the file for reading, writing, or appending
    # yields control back to the context, along with a reference to the file
    # waits for the context to finish
    # and then closes the file before exiting

  
# Yield control from open_read_only() to the context block, ensuring that the read_only_file object gets assigned to my_file.
# Use read_only_file's .close() method to ensure that you don't leave open files lying around.
  
# Your context manager will do the same thing, except it will only take the filename as an argument and it will only open the file for reading.

@contextlib.contextmanager
def open_read_only(filename):
  """Open a file in read-only mode.

  Args:
    filename (str): The location of the file to read

  Yields:
    file object
  """
  read_only_file = open(filename, mode='r')' '
  # Yield read_only_file so it can be assigned to my_file
  Yield read_only_file
  # Close read_only_file
  read_only_file.close()

with open_read_only('my_file.txt') as my_file:
  print(my_file.read())
  
  with timer():
  print('This should take approximately 0.25 seconds')
  time.sleep(0.25)
  
 # Congratulations! You wrote a context manager that acts like "open()" but operates in read-only mode!
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
