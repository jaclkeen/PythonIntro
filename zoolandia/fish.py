from animal import Animal

class Fish(Animal):
    def __init__(self, swimSpeed, maxSwimDepth):
        self.swimSpeed = swimSpeed
        self.maxSwimDepth = maxSwimDepth

    def isSwimming(self):
        return self.name + " is swimming to its max depth of " + str(self.maxSwimDepth) + " ft."

newFish = Fish(10, 30)
newFish.name = "Fred"
print newFish.isSwimming()