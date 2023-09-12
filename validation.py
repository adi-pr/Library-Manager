class DataValidator:
    @staticmethod
    def validate_book(book):
        if not hasattr(book, "title") or not hasattr(book, "author"):
            print("Error: Book must have both title and author")
            return False
        if not isinstance(book.title, str) or not isinstance(book.author, str):
            print("Error: Title and author must be strings")
            return False
        if book.title == "" or book.author == "":
            print("Error: Title and author cannot be empty strings")
            return False
        return True

    @staticmethod
    def validate_member(member):
        if (
            not hasattr(member, "firstName")
            or not hasattr(member, "lastName")
            or not hasattr(member, "gender")
            or not hasattr(member, "emailAddress")
            or not hasattr(member, "phoneNumber")
        ):
            print(
                "Error: Member must have all attributes (firstName, lastName, gender, emailAddress, phoneNumber)"
            )
            return False

        if (
            not isinstance(member.firstName, str)
            or not isinstance(member.lastName, str)
            or not isinstance(member.gender, str)
            or not isinstance(member.emailAddress, str)
            or not isinstance(member.phoneNumber, str)
        ):
            print("Error: All attributes must be strings")
            return False

        if (
            member.firstName == ""
            or member.lastName == ""
            or member.gender == ""
            or member.emailAddress == ""
            or member.phoneNumber == ""
        ):
            print("Error: All attributes cannot be empty strings")
            return False

        valid_genders = ["M", "F", "O"]
        if member.gender not in valid_genders:
            print("Error: Gender must be 'M', 'F', or 'O'")
            return False

        return True
