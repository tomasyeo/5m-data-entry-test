def find_and_replace(lst:list, find_val, replace_val):
"""
Task 1
- Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
- lst must be a list.
- Return the modified list.
"""
if not isinstance(lst, list):
  raise ValueError("The first argument lst must be a list.")
    
# Replace occurrences of find_val with replace_val
return [replace_val if x == find_val else x for x in lst]

# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

if __name__ == '__main__':
  # Output:
  # [1, 5, 3, 4, 5, 5]
  find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
  
  # Output:
  # ['orange', 'banana', 'orange']
  find_and_replace(["apple", "banana", "apple"], "apple", "orange")
