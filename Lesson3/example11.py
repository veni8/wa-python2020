attempts_left = 3
while attempts_left:
    attempts_left -= 1

    password = input('Enter password: ')
    if password == '9a*zx&':
        print('Access granted')
        # do_something()
        break
    else:
        print('Incorrect password')
        print('You have', attempts_left, 'attempts left')
else:
    print('Access denied')
