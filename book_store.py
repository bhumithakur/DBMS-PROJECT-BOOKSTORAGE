from db import DBConnection

class Bookstore:

    def __init__(self):
        print("Management system started")
        self.db = DBConnection("books.db")

        query = '''
        CREATE TABLE IF NOT EXISTS Books(
            name VARCHAR(255),
            author VARCHAR(255),
            publisher VARCHAR(255),
            year_of_publication INTEGER,
            price REAL,
            quantity INTEGER
        );
        '''
        self.db.execute(query)

    
    def add_book(self,name,author,publication,yop,price,quantity):
        query = f'''
        INSERT INTO Books 
        VALUES('{name}','{author}','{publication}',{yop},{price},{quantity});
        '''
        self.db.execute(query)

        print("Book added to inventory!\n")


    def check_quantity(self, name, author, return_records=False):

        query = f'''
        SELECT * FROM Books 
        WHERE name='{name}' AND author='{author}';
        '''
        results = self.db.execute(query)

        if (not results) and (not return_records):
            print('''\nNo such book was found in the inventory!
Please check if you have entered correct details.\n''')
            return

        elif not return_records:
            print(f"\nCopies available = {results[0][5]}")
            print("Book Details -")
            print(f"Name = {results[0][0]}")
            print(f"Author = {results[0][1]}")
            print(f"Publication = {results[0][2]}")
            print(f"Year of publication = {results[0][3]}")
            print(f"Cost of one book = {results[0][4]} Rs.")
            print()
            return
        
        if return_records and results:
            return results[0]
        else:
            return False


    def sell_book(self, name, author):
        record = self.check_quantity(name, author,True)
        if record:
            print(f"{record[5]} copies of the book available")
            n = int(input("Enter number of copies required = "))
            
            diff = record[5] - n
            if diff < 0:
                print("Not enough books!\n")
                return
            elif diff == 0:
                query = f'''
                DELETE FROM Books
                WHERE name='{name}' AND author='{author}';
                '''
            else:
                query = f'''
                UPDATE Books
                SET quantity={diff}
                WHERE name='{name}' AND author='{author}';
                '''
            self.db.execute(query)

            print(f"Total = {record[4] * n} Rs.")
            print("Database updated!\n")
        else:
            print("ERR : Book not found! Check for details entered.\n")


    def list_all_books(self):
        query = '''
        SELECT * FROM Books;
        '''
        results = self.db.execute(query)

        if not results:
            print("ERR : Database is currently empty.\n")
        else:
            print("(Name, Author, Publication, YOP, Price(Rs.), Quantity)")
            for row in results:
                print(row)

if __name__ == "__main__":
    print("Non executable script")