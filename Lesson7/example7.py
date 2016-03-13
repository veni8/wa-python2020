class Base:
    def method(self):
        print('Base method called')


class Child(Base):
    def method(self):
        Base.method(self)
        print('Child method called')


instance = Child()
instance.method()
