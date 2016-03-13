class Person:
    def __init__(self, name):
        self.name = name
        self.siblings = []

    def speak(self):
        print('Hi, I am ' + self.name + '!')

    @staticmethod
    def make_siblings(first, second):
        first.siblings.append(second)
        second.siblings.append(first)


john = Person('John')
linda = Person('Linda')
Person.make_siblings(john, linda)
