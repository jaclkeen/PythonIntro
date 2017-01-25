from animal import Animal

class Bird(Animal):
    def __init__(self, flyDistance, food, name):
        self.flyDistance = flyDistance
        self.food = food
        self.name = name

    def getBirdDistance(self):
        return self.flyDistance

    def isFlying(self):
        return self.name + " is flying!"

newBird = Bird("3 miles!", "Bugs", "Sparky")
print newBird.isFlying()
