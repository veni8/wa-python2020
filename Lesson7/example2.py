class Person:
    def __init__(self, name):
        self.set_name(name)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not name[0].isupper():
            raise ValueError('name must start with a capital letter')
        self.__name = name

    def __repr__(self):
        return 'Person({!r})'.format(self.__name)
