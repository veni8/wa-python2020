class Person:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(self.name, 'is walking')


john = Person('Vasya')
john.walk()  # Person.walk(john)
