class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return 'Rectangle({!r}, {!r})'.format(self.width, self.height)

    def __str__(self):
        # return ('* ' * self.width + '\n') * self.height
        return '\n'.join('* ' * self.width for _ in range(self.height))


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return 'Circle({!r})'.format(self.radius)

    @classmethod
    def from_rectangle(cls, rectangle):
        radius = (rectangle.width ** 2 + rectangle.height ** 2) ** 0.5 / 2
        return cls(radius)
