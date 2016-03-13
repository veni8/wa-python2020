class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('Hi, I am ' + self.name + '!')


john = Person('John')
linda = Person('Linda')

john.speak()
linda.speak()
