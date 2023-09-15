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
        
        title_label = ttk.Label(self.tab, text="Title:", anchor="e")
        self.title_entry = ttk.Entry(self.tab)

        author_label = ttk.Label(self.tab, text="Author:", anchor="e")
        self.author_entry = ttk.Entry(self.tab)

        button_commit = ttk.Button(self.tab, text="Add Book", command=self.addBook)

        title_label.grid(row=0, column=0, padx=15, pady=15)
        self.title_entry.grid(row=0, column=1, padx=15, pady=15)

        author_label.grid(row=1, column=0, padx=15, pady=15)
        self.author_entry.grid(row=1, column=1, padx=15, pady=15)

        button_commit.grid(row=10, column=0, columnspan=2, padx=15, pady=15)
        
    def addBook(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        
        Tabs.library.addBook(title, author)

        
class AddMemberTab: 
    def __init__(self):
        
        self.tab = ttk.Frame(Tabs.tab_control)
        Tabs.tab_control.add(self.tab, text="Add Member")
        
        ttk.Button(self.tab, text="Welcome to the Library Manager").grid(column=0, row=0, padx=30, pady=30)
        
