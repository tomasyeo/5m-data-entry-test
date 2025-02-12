class Car:
  """
  Task 1
  - Define a class named Car with attributes: make, model, year
  - Initialize these attributes in the __init__ method
  - Add a method named describe_car() that prints information about the car as "Year Make Model"
  """
  # Class init.
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
  
  def describe_car(self):
    print(f"Make: {self.year}, Model: {self.make}, Year: {self.model}")

# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020
if __name__ == '__main__':
  # Initialize Car instance.
  car = Car('Toyota', 'Corolla', 2020)
  # Output:
  # Make: 2020, Model: Toyota, Year: Corolla
  car.describe_car()
