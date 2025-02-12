def swap(x, y):
"""
Task 1
- Create a function that would swap the value of x and y using only x and y as variables.
- x and y must be numeric.
- Return -1 if x and y is not numeric, and
- print the swapped values if both x and y are numeric.
"""  
  # Check both x and y are numeric
  if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
    return -1
  
  # Swap values
  x, y = y, x
  
  # Print the swapped values
  print(f"Swapped values: x = {x}, y = {y}")
  
  return x, y


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

if __name__ == '__main__':
  # output: -1
  swap("Apple", 10)

  # output:
  # Swapped values: x = 17, y = 9
  # (17, 9)
  swap(9, 17)

