# Class and object definitions.

# Class Book is initialised with three parameters. The fourth is set 
# by a method.
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.date_finished = "not read"
    
    # Define magic methods for str to print out title/author and page count
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __len__(self):
        return self.pages

# Class PhotoBook inherits from Book and adds another parameter.
class PhotoBook(Book):
    def __init__(self, title, author, pages, subject):
        self.subject = subject
        super().__init__(title, author, pages)
    
    # Override str to also return the book subject
    def __str__(self):
        return f"{self.title} by {self.author} photographs of {self.subject}"

# Test code for Book class
mybook = Book("Targeted", "Brittany Kaiser", 392)
mybook.date_finished = "23-Jan-2020"
print(mybook)
print(len(mybook))
print(mybook.date_finished)

# Test code for PhotoBook class
myphotobook = PhotoBook("Bowie", "Terry O'Neil", 287, "Bowie")
print(myphotobook)
print(len(myphotobook))
print(myphotobook.date_finished)