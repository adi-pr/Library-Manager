from database import Database
from validation import DataValidator


class Library:
    def __init__(self):
        self.database = Database()
        self.validator = DataValidator()

    def addBook(self, title, author, genre):
        book = Book(title, author, genre)

        if self.validator.validate_book(book):
            self.database.writeBook(book)
            self.getAllBooks()

    def removeBook(self, id):
        self.database.removeBook(id)
        self.getAllBooks()
        
    def getAllBooks(self):
        return self.database.getBooks()


    def addMember(self, first_name, last_name, gender, email, phone_number):
        member = Member(first_name, last_name, gender, email, phone_number)

        if self.validator.validate_member(member):
            self.database.writeMember(member)
            self.getAllMembers()
    
    def removeMember(self, id):
        self.database.removeMember(id)
        self.getAllMembers()
    
    def getAllMembers(self):
        return self.database.getMembers()


class Book():
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        
        print(self.genre)


class Member():
    def __init__(self, firstName, lastName, gender, emailAddress, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.emailAddress = emailAddress
        self.phoneNumber = phoneNumber

