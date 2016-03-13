variable = 'global value'


def function():
    variable = 'local value'
    print('[function]', variable)


print('[global]', variable)
function()
