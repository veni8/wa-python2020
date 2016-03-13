from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(number):
    if number <= 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


def fibonacci_iterative(number):
    first, second = 0, 1
    for _ in range(number):
        first, second = second, first + second
    return first


for i in range(1, 101):
    print(fibonacci(i))
