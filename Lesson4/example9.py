def outer_function():
    variable = 'local value of outer_function'

    def inner_function():
        variable = 'local value of inner_function'
        print(variable)

    inner_function()
    print(variable)


outer_function()