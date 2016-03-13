string = input('Enter a string: ')
length = len(string)

if length == 0:
    print('Empty string')
elif length < 15:
    print('Short string')
else:
    print('Long string')
