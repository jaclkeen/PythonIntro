cars = {"Ford", "Chevy", "Toyota", "Nissan", "Ford"}
newCars = {"Test", "Hello"}
junkyard = {"Junk", "POS", "Chevy"}

# Add a car
cars.add("Ford")
# Join two sets together
cars.update(newCars)
# remove item from set
cars.discard("Test")
# Shows the items that are duplicates
print(junkyard.intersection(cars))
print(cars)