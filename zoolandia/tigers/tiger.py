from animals.animal import Animal

class Tiger(Animal):
    def __init__(self):
        self.name = "Unknown tiger"

    def __init__(self, color, favoriteFood, runSpeed):
        self.color = color
        self.favoriteFood = favoriteFood
        self.runSpeed = runSpeed

    def isChasingFood(self):
        return self.name + ", is running " + self.runSpeed + " to catch is favourite food, " + self.favoriteFood