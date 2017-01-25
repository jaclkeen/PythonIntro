class Animal(object):
    def __init__(self, name, height, weight, noise):
        self.name = name
        self.height = height
        self.weight = weight
        self.noise = noise

    def getName(self):
        return self.name

    def getHeight(self):
        return self.height

    def printAnimal(self):
        return "Name: " + self.name + " Height: " + str(self.height) + " Weight: " + str(self.weight) + " Noise: " + self.noise


