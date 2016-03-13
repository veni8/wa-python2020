number = int(input('Number: '))

if number > 5:
    print('[inside if] ', end='')
    print(number, 'is greater than 5')
else:
    print('[inside else] ', end='')
    print(number, 'is less or equal to 5')

print('[outside if]')
