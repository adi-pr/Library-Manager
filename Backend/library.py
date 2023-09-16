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
            self.database.getBooks()

    def getAllBooks(self):
        return self.database.getBooks()

    def removeBook(self, id):
        self.database.removeBook(id)

    def addMember(self):
        member = Member.form_input()

        if self.validator.validate_member(member):
            self.database.writeMember(member)


class Book():
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre.split(',')
        
        print(self.genre)


class Member():
    def __init__(self, firstName, lastName, gender, emailAddress, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.emailAddress = emailAddress
        self.phoneNumber = phoneNumber

