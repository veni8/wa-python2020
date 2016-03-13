class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value[0].isupper():
            raise ValueError('name must start with a capital letter')
        self.__name = value

    def __repr__(self):
        return 'Person({!r})'.format(self.__name)
