class Segment:
    def __init__(self, length):
        self.length = length

    def __repr__(self):
        return 'Segment({!r})'.format(len(self))

    def __str__(self):
        return '-' * len(self)

    def __len__(self):
        return self.length

    def __add__(self, other):
        if type(other) in (int, float):
            result = Segment(len(self))
            result.length += other
            return result
        return Segment(len(self) + len(other))


first = Segment(10)
second = Segment(20)
third = first + second

print(first)
print(second)
print(third)
