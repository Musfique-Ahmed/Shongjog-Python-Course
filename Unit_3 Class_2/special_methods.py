class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"This is a book named {self.title} by {self.author}"

    def __repr__(self):
        return (f"In this instance: title = {self.title}, author = {self.author}")


b1 = Book("The Witches", "Roald")
# b2 = Book("Misir Ali", "Humayun Ahmed")

print(b1)
print(repr(b1))