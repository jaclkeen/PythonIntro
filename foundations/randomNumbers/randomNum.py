import random

random_numbers = list()
for i in range(0, 20, 1):
    random_numbers.append(random.randint(0, 49))

# Comprehension to multiply random numbers by 2
random_numbers = [ num * 2 for num in random_numbers]
print(random_numbers)