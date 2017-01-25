planetList = ["Mercury", "Mars"]
lastPlanets = ["Neptune", "Pluto"]

# Adds item to end of list
planetList.append("Jupiter")
planetList.append("Saturn")

# Adds 2 lists together
planetList.extend(lastPlanets)

# Inserts items to specified index
planetList.insert(1, "Venus")
planetList.insert(2, "Earth")
planetList.insert(6, "Uranus")

rocky_planets = planetList.__getslice__(0, 4)

# Delete pluto
planetList.remove("Pluto")

print planetList