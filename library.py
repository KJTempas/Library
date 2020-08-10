class Book:
    #creating a new class
    def __init__(book, title, author, genre, keywords): #instatiating the class
        book.title = title
        book.author = author
        book.genre = genre
        book.keywords = keywords
       # book.keyword = keyword

    def myfunc(book):  # a method in the Book class
        print("You entered " + book.title + " by " +  book.author)


    books = [] #array to hold all books user inputs

def main():

    try:
        displayMenu()
        while True:
            command = input ("Command: ")
            command = command.lower()
            if command == "add":
                add()
            elif command == "search":
                genreSearch()
            elif command == "delete a book":
                delete()
            elif command == "view":
                view()
            elif command == "exit":
                print("Bye!")
                break
            else:
                print("Not a valid command.  Please try again. \n")
    except KeyError:
        print("Key Error ")

def displayMenu():
    print("OPTION MENU")
    print("add - Add a book")
    print("delete - Delete book")
    print("search- Search books by genre")
    print("view - View books on file")
    print("exit - Exit program")


def add():
    title = input("Enter the title of a book-> ")
    title = title.title()  #make input title case if not already
    author = input("Enter the author of the book in this format - FirstName LastName -> ")
    author= author.title()
    genre = input("Enter the genre of the book  -> ")
    genre = genre.lower()
    #HOW TO HANDLE USER ADDS MORE KEYWORDS or presses space bar to stop
    print("Now you can enter up to 3 keywords for this book.  Press return if you do not have another keyword ")

    keywords = []  # array to hold keywords
    for word in range(3):

        keyword = input("Enter a keyword for this book -> ")
        if keyword =='':  #empty string
            continue
        else:
            keyword =keyword.lower() #make it lower case
            keywords.append(keyword)

    newBook=Book(title, author, genre, keywords) #make a book object w/user input
    Book.books.append(newBook)  #append the new book to the books array in the class Book
    print('You added ' + newBook.title + ' by ' + newBook.author + ' which  is ' + newBook.genre  +
          ' and has these keywords ' + str(newBook.keywords))

def delete():
    title = input("Enter the title of the book you want to delete")
    if title in Book.books:
        Book.books.remove(Book.books)

def genreSearch():
    genre = input("Enter a genre to search -> ")
    genre = genre.lower()  #convert to lower case for comparison
    for book in Book.books: #loop through all of the books in books array
        if (genre in book.genre):
            print('This book has that genre - ' + book.title  + ' by ' + book.author)

def view():
    print("These books are in your book list")
    for book in Book.books:
        print(book.title +  ' by '+  book.author)

main()  #call the main fx