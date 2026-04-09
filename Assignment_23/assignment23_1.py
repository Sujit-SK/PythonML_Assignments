class bookStore:
    # Class variable
    noOfBooks = 0   
    def __init__(self, name, author):
        # Instance variables
        self.name = name
        self.author = author
        bookStore.noOfBooks += 1

    def display(self):
        print(f"{self.name} by {self.author}. No of books:{bookStore.noOfBooks}")

    

def main():
    # Create first object
    obj1 = bookStore("linux","robert love")
    obj1.display()

    obj2 = bookStore("linux","robert lovee")
    obj2.display()
    
    
    

if __name__ == "__main__":
    main()
