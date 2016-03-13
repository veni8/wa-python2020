def factorial_iterative(n):
    result = 1
    for multiplier in range(1, n + 1):
        result *= multiplier
    return result


def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


factorial = factorial_recursive


number = int(input('n = '))
print(factorial(number))