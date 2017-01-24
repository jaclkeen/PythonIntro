# list() - like JS array
# dict() - like JS object
# set() - like JS array, but only contains unique vals
# tuple() - like an immutable list (can't add or remove things from it)
#           is also faster than a list

class Company(object):
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.employees = set()

    def getEmployees(self):
        return self.employees

    def getName(self):
        return self.name

    def addEmployee(self, Employee):
        self.employees.add(Employee)

class Employee(object):
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName


newCompany = Company("Cool Company", "Sells Awesome Products")
newEmployee = Employee("Jacob", "Keen")
anotherEmployee = Employee("Cool", "Guy")

newCompany.addEmployee(anotherEmployee)
newCompany.addEmployee(newEmployee)

for count in newCompany.getEmployees():
    print(count.firstName + " " + count.lastName)