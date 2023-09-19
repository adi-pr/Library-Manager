import tkinter as tk
from tkinter import ttk


class Tabs:
    tab_control = None
    library = None

    def __init__(self, tab_control, library):
        Tabs.library = library
        Tabs.tab_control = tab_control

        self.add_book_tab = AddBookTab()
        self.add_member_tab = AddMemberTab()


class AddBookTab:
    def __init__(self):
        self.tab = ttk.Frame(Tabs.tab_control)
        Tabs.tab_control.add(self.tab, text="Add Book")

        labels = [
            "Title:",
            "Author:", 
            "Genres:" 
        ]

        self.entries = [ttk.Entry(self.tab) for _ in labels]
        
        for i, labels_text in enumerate(labels):
            label = ttk.Label(self.tab, text=labels_text, anchor="e")
            label.grid(row=i, column=0, padx=15, pady=15)
            self.entries[i].grid(row=i, column=1, padx=15, pady=15)

        # Add Book Button
        button_commit = ttk.Button(self.tab, text="Add Book", command=self.addBook)
        button_commit.grid(row=len(labels), column=0, columnspan=2, padx=15, pady=15)

    def addBook(self):
        # Get data from entry bars
        title = self.entries[0].get()
        author = self.entries[1].get()
        genre = self.entries[2].get()

        Tabs.library.addBook(title, author, genre)  # Calls addBook()

        # Clear form upon submit
        for entry in self.entries:
            entry.delete(0, tk.END)


class AddMemberTab:
    def __init__(self):
        self.tab = ttk.Frame(Tabs.tab_control)
        Tabs.tab_control.add(self.tab, text="Add Member")

        labels = [
            "First Name:",
            "Last Name:",
            "Gender:",
            "Email Address:",
            "Phone Number:",
        ]

        self.entries = [ttk.Entry(self.tab) for _ in labels]

        for i, label_text in enumerate(labels):
            label = ttk.Label(self.tab, text=label_text, anchor="e")
            label.grid(row=i, column=0, padx=15, pady=15)
            self.entries[i].grid(row=i, column=1, padx=15, pady=15)

        button_commit = ttk.Button(self.tab, text="Add Member", command=self.addMember)
        button_commit.grid(row=len(labels), column=0, columnspan=2, padx=15, pady=15)

    def addMember(self):
        first_name = self.entries[0].get()
        last_name = self.entries[1].get()
        gender = self.entries[2].get()
        email = self.entries[3].get()
        phone_number = self.entries[4].get()

        Tabs.library.addMember(first_name, last_name, gender, email, phone_number)

        for entry in self.entries:
            entry.delete(0, tk.END)
