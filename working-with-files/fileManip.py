# 3: open(filename) gets elements in txt file, 'r' is for read
# 4: prints all animals that were in the text file
animals = open("animals.txt", 'r')
print (animals.read())
animals.close()

# 8: prints first line of txt file
# print (animals.readline())

# 12: loops through animals in txt file and prints to console
animals = open("animals.txt", 'r')
for animal in animals:
    print("This is a {0}".format(animal))
animals.close()

# 19: gets elements in txt file, 'w' is for write to completely overwrite list with something new
# 20: Clears everything in txt file and adds Crocodile to it
# 21: Closes file
AddAnimals = open("animals.txt", 'w')
AddAnimals.write("Crocodile")
AddAnimals.close()

# 26: opens animals.txt to append to iter
# 27: appends Big bear to the end of the list
# 28: closes the file
AddAnimalToList = open("animals.txt", 'a')
AddAnimalToList.write(" Big Bear")
AddAnimalToList.close()

def readAnimals():
  with open("animals.txt", "r") as animals:
    animalSet = { animal.title() for animal in animals }

  return animalSet

print readAnimals()