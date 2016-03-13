class AttributeContainer:
    value = 'some attribute'


first_instance = AttributeContainer()
second_instance = AttributeContainer()


def print_value():
    print(AttributeContainer.value)
    print(first_instance.value)
    print(second_instance.value)
    # print(AttributeContainer.__dict__)
    # print(first_instance.__dict__)
    # print(second_instance.__dict__)
    print()


print_value()

AttributeContainer.value = 'class attribute'
print_value()

first_instance.value = 'data attribute'
print_value()
