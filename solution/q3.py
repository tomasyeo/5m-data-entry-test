def update_dictionary(dct:dict, key, value):
  """
  Task 1
  - Create a function that updates a dictionary (dct) with a new key-value pair.
  - If the key already exists in dct, print the original value, then update its value.
  - Return the updated dictionary.
  """
  # Check Key in dct.
  if key in dct:
      # Print the original value
      print(f"original value for key '{key}': {dct[key]}")
  
  # Update the dct with new value.
  dct[key] = value
  
  return dct

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26
if __name__ == '__main__':
  # Output:
  # {'name': 'Alice'}
  update_dictionary({}, "name", "Alice")

  # Output:
  # original value for key 'age': 25
  # {'age': 26}
  update_dictionary({"age": 25}, "age", 26)
