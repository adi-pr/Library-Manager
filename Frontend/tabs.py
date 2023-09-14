from tkinter import ttk

class Tabs:
    tab_control = None
    library = None
    
    def __init__(self, tab_control, library):
        Tabs.library = library
        Tabs.tab_control = tab_control
        
        self.tab1 = Tab1()
        self.tab2 = Tab2()
        

class Tab1(Tabs): 
    def __init__(self):
        
        self.tab = ttk.Frame(Tabs.tab_control)
        Tabs.tab_control.add(self.tab, text="Add Book")
        
        ttk.Button(self.tab, text="Add Book", command=Tabs.library.addBook).grid(column=0, row=0, padx=30, pady=30)

        
class Tab2(Tabs): 
    def __init__(self):
        
        self.tab = ttk.Frame(Tabs.tab_control)
        Tabs.tab_control.add(self.tab, text="Add Book")
        
        ttk.Button(self.tab, text="Welcome to the Library Manager").grid(column=0, row=0, padx=30, pady=30)
        
