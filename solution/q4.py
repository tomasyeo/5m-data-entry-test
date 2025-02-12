def string_reverse(s:str):
  """
  Task 1
  - Create a function that reverses a given string (s).
  - s must be a string.
  - Return the reversed string.
  """
  # Check if s is a string
  if not isinstance(s, str):
      raise ValueError("input not a string.")
  
  # Return reversed string  
  return s[::-1]

# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
if __name__ == '__main__':
  # Output:
  # 'dlroW olleH'
  string_reverse("Hello World")

  # Output:
  # 'nohtyP'
  string_reverse("Python")
