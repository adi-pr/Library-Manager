import sys
import tkinter as tk

path = sys.path.insert(0, "Backend")
from library import Library


class Interface:
    def __init__(self, root, library):
        self.root = root
        self.root.title("Library Manager")
        self.library = Library()

        self.add_book = tk.Button(
            self.root,
            text="Add Book",
            command=library.addBook
        )
        self.add_book.pack()

if __name__ == "__main__":
    root = tk.Tk()
    library = Library()

    interface = Interface(root, library)

    root.mainloop()
