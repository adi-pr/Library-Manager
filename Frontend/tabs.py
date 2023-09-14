from tkinter import ttk

class Tabs:
    def __init__(self, tab_control, library):
        self.library = library
        self.tab_control = tab_control
        
        self.tab1 = Tab1(self.tab_control)
        self.tab2 = Tab2(self.tab_control)
        

class Tab1: 
    def __init__(self, tab_control):
        self.tab_control = tab_control
        
        self.tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab, text="Add Member")
        
        ttk.Label(self.tab, text="Welcome to the Library Manager").grid(column=0, row=0, padx=30, pady=30)
        
class Tab2: 
    def __init__(self, tab_control):
        self.tab_control = tab_control
        
        self.tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab, text="Add Book")
        
        ttk.Label(self.tab, text="Built by Ruben").grid(column=0, row=0, padx=30, pady=30)