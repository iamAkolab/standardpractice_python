# Crafting a docstring

You've decided to write the world's greatest open-source natural language processing Python package
The first function you write is count_letter(). It takes a string and a single letter and returns the number of times the letter appears in the string. 
You want the users of your open-source package to be able to understand how this function works easily, so you will need to give it a docstring. 
Build up a Google Style docstring for this function by following these steps.


def count_letter(content, letter):
  """Count the number of times `letter` appears in `content`.

  Args:
    content (str): The string to search.
    letter (str): The letter to search for.

  Returns:
    int

  # Add a section detailing what errors might be raised
  Raises:
    ValueError: If `letter` is not a one-character string.
  """
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('`letter` must be a single character string.')
  return len([char for char in content if char == letter])
  
# Retrieving docstrings
 
You and a group of friends are working on building an amazing new Python IDE (integrated development environment -- like PyCharm, Spyder, Eclipse, Visual Studio, etc.). The team 
wants to add a feature that displays a tooltip with a function's docstring whenever the user starts typing the function name. That way, the user doesn't have to go elsewhere to 
look up the documentation for the function they are trying to use. You've been asked to complete the build_tooltip() function that retrieves a docstring from an arbitrary function.

You will be reusing the count_letter() function that you developed in the last exercise to show that we can properly extract its docstring
Begin by getting the docstring for the function
# Get the "count_letter" docstring by using an attribute of the function
docstring = count_letter.__doc__

border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))
############################
Count the number of times `letter` appears in `content`.

  Args:
    content (str): The string to search.
    letter (str): The letter to search for.

  Returns:
    int

  Raises:
    ValueError: If `letter` is not a one-character string.
  
############################
