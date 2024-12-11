import csv
#Final Project for Data Structure
#Library Records

#Bill's and Nayeem's work
class Book:
    def __init__(self, title, author, genre, status='unread', rating=None):
        self.title = title  # Stores the title of the book
        self.author = author  # Stores the author of the book
        self.genre = genre  # Stores the genre of the book
        self.status = status  # Stores the reading status: 'read' or 'unread'
        self.rating = rating  # Stores the optional rating for the book
        self.next = None  # Points to the next book in the linked list


    #This is Bill's work

    def setTitle(self, title): #Set the title of the book
        self.title = title
    
    def setAuthor(self, author): #set the author of the book
        self.author = author
    
    def setPages(self, pages): #Set the amount of pages in the book
        self.pages = pages

    def setPrice(self, price): #set the price of the book
        self.price = price
    
    def getTitle(self): #Get the title of the book
        return self.title
    
    def getAuthor(self): #Get the author of the book
        return self.author
    
    def getPages(self): #Get the amount of pages in the book
        return self.pages
    
    def getPrice(self): #Get the price of the book
        return self.price
    
    def markAsRead(self, read): #Set the read to True if read
        self.read = True

    def setGenre(self, genre): #Set the genre of the book
        self.genre = genre
    
    def getGenre(self): #Get the genre of the book
        return self.genre
    
    def purchased(self, count): #collects the amount of time a book has been purchased
        self.count += count

    def getCount(self): #get the amount of times the book has been purchased
        return self.count

    def description(self): #Print out the description
        return (f"Title:{self.title} \nAuthor:{self.author} \nPages:{self.pages} \nGenre:{self.genre if self.genre else 'Not Specific'} \nRead:{self.read} \nPrice:{self.price} \nPurchases:{self.count}")


def getBooks():
    hammerAndTheElixir = Book("Hammer and the Elixir", "Alia Knight", "657", "Fantasy")
    deathofthestuffedFalcon = Book("Death of the Stuffed Falcon", "Adam Ramsey", "971", "Sci-fi" )
    bestBeloved = Book("Best Beloved", "Kadie Hebert", "466", "Romance")
    theSonsoftheFrontier = Book("The Sons of the Frontier", "Johnny Robinson", "675", "Historical-Fiction")
    theHolidayBride = Book("The Holiday Bride", "Tatiana Washington", "207", "Romance")
    callOfQueens = Book("Call of Queens", "Lily-Rose Hendricks", "342", "Fantasy")
    beta2099 = Book("2099: Beta", "Wiktor Bradley", "884", "Sci-fi")
    swordsBook = Book("Sword's Book", "Nathan Dixon", "589", "Fantasy")
    greaterPower = Book("A Greater Power", "Amber Jones", "344", "Psychological")
    brideinthefog = Book("The Bride in the Fog", "Hasan Tapia", "569", "Romance")
    bamWentMyHeart = Book("Bam Went My Heart", "Callum Mcbride", "369", "Romance")
    markedForError = Book("Marked for Error", "Jayson Schaefer", "713", "Psychological")
    signOfSilence = Book("Sign of Silence", "Abdulrahman Guzman", "409", "Thriller")
    theHeartoftheNameless = Book("The Heart of the Nameless", "Lucinda Andrews", "322", "Psychological")
    theDevilsGift = Book("The Devil's Gift", "Lacie Neal", "580", "Sci-fi")
    blueShadow = Book("Blue Shadow", "Soraya Mckenzie", "623", "Thriller")
    maskOfIron = Book("Mask of Iron", "Aryan Campos", "618", "Psychological" )
    theRavenDream = Book("The Raven's Dream", "Melvin Beck", "906", "Romance")
    theBruteinthePainting = Book("The Brute in the Painting", "Holly Farrell", "440", "Psychological")
    dynamiteTouch = Book("Dynamite Touch","Elsie Brock", "847", "Sci-fi")
    circleofEarth = Book("The Circle of Earth That Was", "Taylor Wilkson", "374", "Historical-Fiction")
    strangerinthenight = Book("The Stranger in the Night", "Scott Lang", "841", "Romance")
    judgeforCarnage = Book("Judged for Carnage","Ruth Haynes", "599", "Thriller")
    
    bookshelf = [hammerAndTheElixir, deathofthestuffedFalcon, bestBeloved, theSonsoftheFrontier, theHolidayBride, callOfQueens, beta2099, swordsBook, 
                 greaterPower, brideinthefog, bamWentMyHeart, markedForError, signOfSilence, theHeartoftheNameless, theDevilsGift, 
                 blueShadow, maskOfIron, theRavenDream, theBruteinthePainting, dynamiteTouch, circleofEarth, strangerinthenight, judgeforCarnage]
    
    return bookshelf
        
getBooks()

#Alejandro's work
class Queue:
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def enqueue(self, object):
        self.queue.append(object)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop()
        else:
            return None
    
    def peekQueue(self):
        if not self.isEmpty():
            return self.queue[-1]
        else:
            return None
        
class Node:
    def __init__(self, value = None, next = None, previous = None):
        self._value_ = value
        self._next_ = next
        self._previous_ = previous
        return
    
    def set(self, value):
        self._value_ = value

    def get_value(self):
        # Return the value of this node
        return self.__value__
    
    def get_next(self):
        # Return this node's next node
        return self.__next__
    
    def get_previous(self):
        # Return this node's previous node
        return self.__previous__
    
    def set_next(self, next):
        # Set this node's next node
        self.__next__ = next
        # Return this node
        return
    
    def set_previous(self, previous):
        # Set this node's previous node
        self.__previous__ = previous
        # Return this node
        return


# Linked List
# This class manages a list of books, allowing books to be added, deleted, or displayed.
class LinkedList:
    def __init__(self):
        self.head = None  # Stores the start of the linked list (initially empty)

    # Adds a book to the end of the linked list
    def add(self, book):
        if not self.head:
            self.head = book  # Sets the new book as the head if the list is empty
        else:
            current = self.head
            while current.next:  # Traverses to the end of the list
                current = current.next
            current.next = book  # Sets the new book at the end of the list

    # Deletes a book by title from the linked list
    def delete(self, title):
        current = self.head
        previous = None
        while current:
            if current.title == title:  # Finds the book with the matching title
                if previous:  # If it's not the head, adjusts the pointers
                    previous.next = current.next
                else:  # If it's the head, updates the head pointer
                    self.head = current.next
                return f"Book '{title}' deleted."
            previous = current  # Moves to the next node
            current = current.next
        return f"Book '{title}' not found."  # Indicates that the book was not found

    # Displays all books in the linked list as a list
    def display(self):
        books = []
        current = self.head
        while current:
            books.append(current)  # Collects each book in the list
            current = current.next
        return books


#Final project practice (not the main program just evidence of participation for Nayem)

# Library Management System
# This class manages the entire library, using a dictionary of linked lists to organize books by genre.
class Library:
    def __init__(self):
        self.genres = {}  # Stores genres as keys and linked lists as values

    # Adds a book to the library under the appropriate genre
    def add_book(self, title, author, genre, status='unread', rating=None):
        book = Book(title, author, genre, status, rating)  # Creates a new Book object
        if genre not in self.genres:  # Checks if the genre exists; if not, creates a new linked list
            self.genres[genre] = LinkedList()
        self.genres[genre].add(book)  # Adds the book to the linked list for the genre
        return f"Book '{title}' added to genre '{genre}'."

    # Deletes a book from the library by searching across all genres
    def delete_book(self, title):
        for genre, linked_list in self.genres.items():  # Iterates through all genres
            result = linked_list.delete(title)  # Tries to delete the book from the current genre
            if "deleted" in result:  # Checks if the deletion was successful
                return result
        return f"Book '{title}' not found."  # Indicates that the book was not found in any genre

    # Searches for books by keyword (matches title or author)
    def search_books(self, keyword):
        results = []
        for genre, linked_list in self.genres.items():  # Iterates through all genres
            current = linked_list.head
            while current:
                # Checks if the keyword matches the book's title or author
                if keyword.lower() in current.title.lower() or keyword.lower() in current.author.lower():
                    results.append(current)  # Adds matching books to the results
                current = current.next  # Moves to the next book
        return results

    # Counts the number of unread books using recursion
    def count_unread_books(self):
        def recursive_count(node):
            if not node:  # Base case: if the node is None, returns 0
                return 0
            # Adds 1 if the book is unread, then recursively counts the rest
            return (1 if node.status == 'unread' else 0) + recursive_count(node.next)

        total = 0
        for linked_list in self.genres.values():  # Counts unread books for each genre
            total += recursive_count(linked_list.head)
        return total

    # Displays all books in the library, organized by genre
    def display_library(self):
        for genre, linked_list in self.genres.items():  # Iterates through all genres
            print(f"\nGenre: {genre}")
            for book in linked_list.display():  # Displays all books in the genre
                print(f" - {book.title} by {book.author} [{book.status}]")

#Jonas's work------------------------

def load_data(file_path):
    data = []
    headers = None
    try:
        #open and read the file
        with open(file_path, mode='r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # Read the header row
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return headers, data


def linear_search(data, bookName):
    try:
        if not data:
            raise ValueError("No data available to search.")

        # Perform the linear search
        for row in data:
            if str(row[0]).strip().lower() == bookName.strip().lower():
                return row  # Book found, return the row

        return None  # Book not found
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An error occurred during the search: {e}")
    return None  # Return None if there's an error or no match found


def search_for_book(file_path, bookName):
    # Load data from the CSV file
    headers, data = load_data(file_path)
    
    if not data:
        print("No data available to search.")
        return None
    
    # Perform the book search
    result = linear_search(data, bookName)
    
    if result:
        return result  # Return the found book
    else:
        print("Book not found.")
        return None

def sort_books_by_pages(file_path):
    # Load data from CSV file
    headers, data = load_data(file_path)
    
    if not data:
        print("No data available to sort.")
        return []
    
    try:
        sorted_data = sorted(data, key=lambda row: int(row[2]), reverse=False)
        return sorted_data
    except IndexError:
        print("Error: Page count column does not exist.")
        return []
    except ValueError:
        print("Error: Non-numeric value found in page count column.")
        return []
    
# Example usage
book = search_for_book('bookshelf.csv', "The Heart of the Nameless")
if book:
    print(f"Book found: {book}")
 
sorted_books = sort_books_by_pages('bookshelf.csv')
if sorted_books:
    print("Books sorted by page count:")
    for book in sorted_books:
        print(book)
else:
    print("No books to display.")

# Main Function
# This is the entry point for the program and provides a menu-driven interface for the user.
def main():
    library = Library()  # Creates a Library object
    while True:
        # Displays the main menu
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Search Books")
        print("4. Count Unread Books")
        print("5. Display Library")
        print("6. Exit")
        choice = input("Enter your choice: ")

        # Performs actions based on the user's choice
        if choice == '1':
            # Adds a new book
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            genre = input("Enter genre: ")
            status = input("Enter status (read/unread): ")
            rating = input("Enter rating (optional): ")
            print(library.add_book(title, author, genre, status, rating))

        elif choice == '2':
            # Deletes a book
            title = input("Enter book title to delete: ")
            print(library.delete_book(title))

        elif choice == '3':
            # Searches for books
            keyword = input("Enter search keyword: ")
            results = library.search_books(keyword)
            if results:
                for book in results:
                    print(f" - {book.title} by {book.author} [{book.status}]")
            else:
                print("No books found.")

        elif choice == '4':
            # Counts unread books
            print(f"Unread books: {library.count_unread_books()}")

        elif choice == '5':
            # Displays all books in the library
            library.display_library()

        elif choice == '6':
            # Exits the program
            print("Goodbye!")
            break

        else:
            # Handles invalid input
            print("Invalid choice. Please try again.")


# Directly calls the main function to start the program
main()