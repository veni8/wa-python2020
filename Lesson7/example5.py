class Horse:
    def run(self):
        print('I am running')


class Bird:
    def fly(self):
        print('I am flying')


class Pegasus(Horse, Bird):
    pass
