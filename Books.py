class Book: 
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.read = False
        self.price = 0
        self.count = 0
        self.genre = genre

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