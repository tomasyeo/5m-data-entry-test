def check_divisibility(num, divisor):
"""
Task 1
- Create a function to check if the number (num) is divisible by another number (divisor).
- Both num and divisor must be numeric.
- Return True if num is divisible by divisor, False otherwise.
"""
  # Check num and divisor are numeric.
  if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
    raise ValueError("num and divisor must be numeric.")
  
  # True if divisible, else False
  return num % divisor == 0

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
if __name__ == '__main__':
  # Output: True
  check_divisibility(10, 2)

  # Output: False
  check_divisibility(7, 3)
