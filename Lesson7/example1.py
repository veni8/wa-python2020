class Base:
    def __init__(self):
        self.public_variable = 'Base public value'
        self._protected_variable = 'Base protected value'
        self.__private_variable = 'Base private value'

    def print_values(self):
        print('Public:', self.public_variable)
        print('Protected:', self._protected_variable)
        print('Private:', self.__private_variable)


class Child(Base):
    def __init__(self):
        Base.__init__(self)
        self.public_variable = 'redefined public'
        self._protected_variable = 'redefined protected'
        self.__private_variable = 'redefined private'

    def print_private(self):
        print('Child private:', self.__private_variable)


base_instance = Base()
child_instance = Child()

base_instance.print_values()
print()
child_instance.print_values()
child_instance.print_private()
