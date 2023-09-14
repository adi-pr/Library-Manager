import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tabs import Tabs

# Import Library Class
path = sys.path.insert(0, "Backend")
from library import Library


class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Manager")
        self.library = Library()

        self.tab_control = ttk.Notebook(root)

        self.tabs = Tabs(self.tab_control, self.library)

        self.tab_control.pack(expand=1, fill="both")


if __name__ == "__main__":
    root = tk.Tk()
    interface = Interface(root)

    root.mainloop()
