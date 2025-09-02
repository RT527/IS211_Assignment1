#Rafi Talukder
class Book:
    def __init__(self, author, title): # Two attributes author + title
        self.author = author #str for book author
        self.title = title #str for book title

    def display(self): # Prints out string representation of book
        print(f'"{self.title}", written by {self.author}')

if __name__ == "__main__":
    a = Book("Thorpe", "Beat the Dealer")
    print("This is a assignment 1 part 2")

    # Instantiate 2 books
    magic_orphan = Book("J.K. Rowling", "Harry Potter and the Goblet of Fire")
    love_maybe = Book("Walter Scott", "Ivanhoe: A Romance")
    # Now we call the display() method for each of the objects so they print
    magic_orphan.display()
    love_maybe.display()