class Book:
    """Класс, представляющий книгу
    """

    def __init__(self, title, year, genre):
        """Конструктор

        Задание: сохраните title, year и genre в виде
        атрибутов объекта self
        :rtype: object
        """
        self.title = title
        self.year = year
        self.genre = genre


    def __repr__(self):
        """Возвращает внутреннее строковое представление объекта
        для консоли, отладчика и т.д.

        Задание: верните строку в формате
                 Book("название", год, "жанр")
        """
        return 'Book({!r},{!r},{!r})'.format(self.title, self.year, self.genre)

    def __str__(self):
        """Возвращает строку, предназначенную для пользователя
        (str, print и т.д.)

        Задание: верните строку в произвольном формате
        """
        return 'Book-! ({!r},{!r},{!r})'.format(self.title, self.year, self.genre)


# Задание: создайте несколько объектов класса Book
# и выведите их на экран
a1 = Book("Fas", 1998, "df")
b1 = Book("dc", "2", "d")
print(a1)
print(b1)




