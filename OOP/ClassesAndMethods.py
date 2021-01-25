class Person:

    def __init__(self, name):
        self.name = name

    def printName(self):
        return self.name

p = Person('Aditya')
print(p.printName())
