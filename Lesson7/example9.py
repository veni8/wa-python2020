class Animal:
    def __init__(self):
        self.can_run = False
        self.can_fly = False

    def print_abilities(self):
        print(type(self).__name__, 'can:',)
        if self.can_run:
            print(' - run')
        if self.can_fly:
            print(' - fly')
        print()


class Bird(Animal):
    def __init__(self):
        super().__init__()
        self.can_fly = True


class Horse(Animal):
    def __init__(self):
        super().__init__()
        self.can_run = True


class Pegasus(Horse, Bird):
    pass


horse = Horse()
bird = Bird()
pegasus = Pegasus()

horse.print_abilities()
bird.print_abilities()
pegasus.print_abilities()
