from animals.animal import Animal

class Fish(Animal):
    def __init__(self):
        self.name = "Unknown fish"

    def __init__(self, swimSpeed, maxSwimDepth):
        self.swimSpeed = swimSpeed
        self.maxSwimDepth = maxSwimDepth

    def isSwimming(self):
        return self.name + " is swimming to its max depth of " + str(self.maxSwimDepth) + " ft."

    def printAnimal(self):
        return self.name + " can swim " + str(self.swimSpeed) + " mph!"