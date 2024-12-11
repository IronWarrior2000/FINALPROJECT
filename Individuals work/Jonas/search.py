import csv


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
