import math

class Shape(object):
    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth

    def getVolume(self):
        return self.height * self.width * self.depth

class Cube(Shape):
    def __init__(self, height, width, depth):
        super(Cube, self).__init__(height, width, depth)

class Cylinder(Shape):
    def __init__(self, height, width, depth):
        super(Cylinder, self).__init__(height, width, depth)

    def getVolume(self):
        return 3.14 * (math.pow(self.width / 2, 2)) * self.height

class Pyramid(Shape):
    def __init__(self, height, width, depth):
        super(Pyramid, self).__init__(height, width, depth)

    def getVolume(self):
        return .333 * (math.pow(self.width, 2)) * self.height

def CreateShape(input, shapeValsList):
    if(input == 1):
        shape = Pyramid(shapeValsList[0], shapeValsList[1], shapeValsList[2])
        return shape
    elif(input == 2):
        shape = Cube(shapeValsList[0], shapeValsList[1], shapeValsList[2])
        return shape
    else:
        shape = Cylinder(shapeValsList[0], shapeValsList[1], shapeValsList[2])
        return shape

def Execute():
    shapeInput = raw_input("Select a shape: \n  1. Pyramid \n  2. Cube \n  3. Cylinder \n")
    shapeVals = raw_input("Enter the height, width, and volume in that order and seperated by commas: ")
    shapeValsList = map(int, shapeVals.split(","))
    createdShape = CreateShape(int(shapeInput), shapeValsList)
    print createdShape.getVolume()

Execute()