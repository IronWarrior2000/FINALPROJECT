class Queue:
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def enqueue(self, user):
        self.queue.append(user)
        print(f"{user} added to the borrowing queue.")
    
    def dequeue(self):
        if not self.isEmpty():
            user = self.queue.pop(0)
            print(f"{user} has been served and removed from the queue.")
            return user
        else:
            print("No users in the queue.")
            return None
    
    def peekQueue(self):
        if not self.isEmpty():
            print(f"Next in line: {self.queue[0]}")
            return self.queue[0]
        else:
            print("Queue is empty.")
            return None
    
    def queueSize(self):
        print(f"Number of people in the queue: {len(self.queue)}")
        return len(self.queue)

# Simulating book borrowing process
def borrowBook(book_title, queue):
    # Try to dequeue the first person from the queue for this book
    if queue.isEmpty():
        print(f"No users in the queue for {book_title}.")
    else:
        user = queue.dequeue()
        print(f"{user} has borrowed the book: {book_title}")

# Example of how it could work
if __name__ == "__main__":
    book_queue = Queue()

    # Add users to the queue
    book_queue.enqueue("User1")
    book_queue.enqueue("User2")
    book_queue.enqueue("User3")

    # Peek who is next in the queue
    book_queue.peekQueue()

    # Simulate borrowing the book
    borrowBook("Hammer and the Elixir", book_queue)
    borrowBook("Death of the Stuffed Falcon", book_queue)
    borrowBook("Best Beloved", book_queue)
    borrowBook("The Sons of the Frontier", book_queue)
    borrowBook("The Holiday Bride", book_queue)
    borrowBook("Call of Queens", book_queue)
    borrowBook("2099: Beta", book_queue)
    borrowBook("Sword's Book", book_queue)
    borrowBook("A Greater Power", book_queue)
    borrowBook("The Bride in the Fog", book_queue)
    borrowBook("Bam Went My Heart", book_queue)
    borrowBook("Marked for Error", book_queue)
    borrowBook("Sign of Silence", book_queue)
    borrowBook("The Heart of the Nameless", book_queue)
    borrowBook("The Devil's Gift", book_queue)
    borrowBook("Blue Shadow", book_queue)
    borrowBook("Mask of Iron", book_queue)
    borrowBook("The Raven's Dream", book_queue)
    borrowBook("The Brute in the Painting", book_queue)
    borrowBook("Dynamite Touch", book_queue)
    borrowBook("The Circle of Earth That Was", book_queue)
    borrowBook("The Stranger in the Night", book_queue)
    borrowBook("Judged for Carnage", book_queue)
    

    
        
