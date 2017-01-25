class Aquarium:
    animalsInAquarium = list()

    def __init__(self):
        self = self

    def __init__(self, Animal):
        self.animalsInAquarium.append(Animal)

    def getAnimals(self):
        return self.animalsInAquarium

    def addAnimal(self, Animal):
        self.animalsInAquarium.append(Animal)