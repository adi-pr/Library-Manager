from abc import ABCMeta, abstractclassmethod
from database import Database
from validation import DataValidator


class InputSource(metaclass=ABCMeta):
    @abstractclassmethod
    def form_input(cls):
        pass


class Library:
    def __init__(self, database):
        self.database = database
        self.validator = DataValidator()

    def addBook(self):
        book = Book.form_input()

        if self.validator.validate_book(book):
            self.database.writeBook(book)

    def getAllBooks(self):
        return self.database.getBooks()

    def removeBook(self, id):
        self.database.removeBook(id)

    def addMember(self):
        member = Member.form_input()

        if self.validator.validate_member(member):
            self.database.writeMember(member)


class Book(InputSource):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def form_input(cls):
        title = input("Title of Book: ")
        author = input("Author of Book: ")
        return cls(title, author)


class Member(InputSource):
    def __init__(self, firstName, lastName, gender, emailAddress, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.emailAddress = emailAddress
        self.phoneNumber = phoneNumber

    @classmethod
    def form_input(cls):
        firstName = input("First Name: ")
        lastName = input("Last Name: ")
        gender = input("Gender (M, F, O): ")
        emailAddress = input("Email: ")
        phoneNumber = input("Phone Number: ")
        return cls(firstName, lastName, gender, emailAddress, phoneNumber)
