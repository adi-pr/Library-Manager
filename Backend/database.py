import mysql.connector


class Database:
    _instance = None
    connection = mysql.connector.connect(
        host="localhost", user="root", password="root", database="library"
    )
    cursor = connection.cursor()

    # Checks if an instance exist already
    def __new__(cls, *args, **kwargs):
        if not Database._instance:
            # Creates Database class if there isn't an existing instance and creates tables
            Database._instance = super(Database, cls).__new__(cls, *args, **kwargs) 
            Database.createTables(cls)
            
        return Database._instance # Return the already existing instance

    def createTables(self):
        print("Creating Tables")
        try:
            # Create 'books' table if none exits
            self.cursor.execute(
                "CREATE TABLE IF NOT EXISTS books (id int PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(255), author VARCHAR(255), genre VARCHAR(255) )"
            )
            print("Tables Created ")
            # Create 'members' table if none exits
            self.cursor.execute(
                "CREATE TABLE IF NOT EXISTS members (id int PRIMARY KEY NOT NULL AUTO_INCREMENT, firstName VARCHAR(255) NOT NULL, lastName VARCHAR(255) NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL, emailAddress VARCHAR(255), phoneNumber VARCHAR(255) NOT NULL)"
            )
        except:
            # Roll back database if an error occurs
            self.connection.rollback()
            print("An Error Occurred While Creating Tables")
        return self.cursor

    # Outputs all books
    def getBooks(self):
        self.cursor.execute("SELECT * FROM books")

        for x in self.cursor:
            print(x)

    # Adds a book to the database
    def writeBook(self, book):
        self.cursor.execute(
            "INSERT INTO books (name, author) VALUES (%s, %s)", (book.title, book.author)
        )
        print(f"Book: {book.title} added ")
        self.connection.commit()

    # Removes a book from the database 
    def removeBook(self, id):
        print("Removing Book --")
        try:
            self.cursor.execute(f"DELETE FROM books WHERE id = {id}")
            self.connection.commit()
            print("Book Removed Successfully --")
        except:
            # Roll back in the event an error occurs
            self.connection.rollback()
            print(f"An Error Occurred While Removing Book: {id}")


    def getMembers(self):
        self.cursor.execute("SELECT * FROM members")

        for x in self.cursor:
            print(x)
            
    def writeMember(self, member):
        self.cursor.execute(
            "INSERT INTO members (firstName, lastName, gender, emailAddress, phoneNumber) VALUES (%s, %s, %s, %s, %s)", (member.firstName, member.lastName, member.gender, member.emailAddress, member.phoneNumber)
        )
        print(f"Added Member: {member.firstName}")
        self.connection.commit()