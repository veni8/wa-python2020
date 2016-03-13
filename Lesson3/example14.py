for attempts_left in range(3, 0, -1):
    password = input('Enter password: ')
    if password == '9a*zx&':
        print('Access granted')
        # do_something()
        break
    else:
        print('Incorrect password')
        print('You have', attempts_left - 1, 'attempts left')
else:
    print('Access denied')
