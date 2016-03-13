def Person(name, age):
    def greet():
        print('Hello!')
        print('My name is', name + '.')

    return {
        'greet': greet,
        'age': age
    }


john = Person('John', 28)
john['greet']()
print('Age:', john['age'])

print()

vasya = Person('Vasya', 29)
vasya['greet']()
