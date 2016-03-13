elem = lambda value, next: {'value': value, 'next': next}
to_string = lambda head: '' if head is None \
                            else str(head['value']) + ' ' + to_string(head['next'])

values = elem(1, elem(2, elem(3, None)))
print(to_string(values))

###

class Element:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class List:
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            for value in iterable:
                self.append(value)

    def append(self, value):
        elem = Element(value)
        if not self.head:
            self.head = self.tail = elem
        else:
            self.tail.next = elem
            self.tail = elem

    def __str__(self):
        result = ''
        elem = self.head
        while elem:
            result += str(elem.value) + ' '
            elem = elem.next
        return result


values = List([1, 2, 3])
print(values)
