class Animal:
    def eat(self, food):
        print('This animal is eating', food)


class Bird(Animal):
    def fly(self):
        print('Bird is flying')


class Horse(Animal):
    def run(self):
        print('Horse is running')


class Food:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        animal.eat(self)

    def __str__(self):
        return self.name


banana = Food('bananas')
horse = Horse()
banana.feed_animal(horse)

horse.eat()
