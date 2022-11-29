from book_store import Bookstore

bs = Bookstore()

print('''
    Following actions can be performed by entering choice 
    after being prompted - \n
    >> Enter "1" to add a book
    >> Enter "2" to check for a book
    >> Enter "3" to sell a book
    >> Enter "4" to see the list of all books available
    >> Enter "5" to exit the program
    ''')

while True:
    op = input("Enter choice - ")

    if op == '1':
        print("ADDING BOOK DATA...")
        name = input("Enter book name = ")
        author = input("Enter author name = ")
        publication = input("Enter publication name = ")
        yop = input("Enter year of publication = ")
        price = input("Enter price of the book = ")
        quantity = input("Enter number of books to add = ")
        bs.add_book(name,author,publication,yop,price,quantity)

    elif op == '2':
        print("FETCHING BOOK DETAILS...")
        name = input("Enter book name = ")
        author = input("Enter author name = ")
        bs.check_quantity(name, author)
    
    elif op == '3':
        print("CHECKING OUT BOOKS...")
        name = input("Enter book name = ")
        author = input("Enter author name = ")
        bs.sell_book(name, author)
    
    elif op == '4':
        print("FETCHING ALL DATA...")
        bs.list_all_books()
        print()

    elif op == '5':
        break

    else:
        print("ERR : Please select a valid option!")

print("Thank you for using the program!!")