class Base:
    def method(self):
        print('Base method called')


class Child(Base):
    def method(self):
        super().method()
        print('Child method called')


instance = Child()
instance.method()
