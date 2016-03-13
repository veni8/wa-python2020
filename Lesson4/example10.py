def make_adder(first):
    def add(second):
        return first + second
    return add


add_to_five = make_adder(5)
print(add_to_five(3))
