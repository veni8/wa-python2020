def enter_number(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print('Incorrect input, try again')
        return enter_number(prompt)


print(enter_number('Enter an integer number: '))
