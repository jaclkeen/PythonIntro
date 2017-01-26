class Savannah:
    animalsInSavannah = list()

    def __init__(self):
        self = self

    def __init__(self, Animal):
        self.animalsInSavannah.append(Animal)

    def getAnimals(self):
        return self.animalsInSavannah

    def addAnimal(self, Animal):
        self.animalsInSavannah.append(Animal)