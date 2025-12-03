

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"key {key} is not found"


book1 = Book("Harry Potter and the Philosopher's Stone",
             "J.K Rowling Lion", 310)
book2 = Book("Harry Potter and the Philosopher's Stone",
             "J.K Rowling Lion", 223)
book3 = Book("Marvel Comics", "Tony Stark", 357)

print(book2)
print(book1 == book2)
print(book2 > book1)
print(book1 + book2)

print("Lion" in book1)

print(book3["audio"])
