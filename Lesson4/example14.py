def hanoi(n, a, b, c):
    if n == 0:
        return
    hanoi(n - 1, a, c, b)
    print('Перенести одно кольцо со стержня {} на стержень {}'.format(a, c))
    hanoi(n - 1, b, a, c)


hanoi(8, 'A', 'B', 'C')
print()
