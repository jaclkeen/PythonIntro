from birds.cardinal import Cardinal
from fish.salmon import Salmon
from tigers.siberian import Siberian
from habitats import aquarium, savannah

newCardinal = Cardinal()

newSalmon = Salmon()
newRedSalmon = Salmon()
newRedSalmon.name = "Red Salmon"
newAquarium = aquarium.Aquarium(newSalmon)
newAquarium.addAnimal(newRedSalmon)

newSiberian = Siberian()
newBengal = Siberian()
newBengal.name = "Fred"
newSavannah = savannah.Savannah(newBengal)
newSavannah.addAnimal(newSiberian)

print "Savannah"
for animal in newSavannah.getAnimals():
    print "    " + animal.name

print "Aquarium: "
for animal in newAquarium.getAnimals():
    print "    " + animal.name
