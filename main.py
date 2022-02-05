import tkinter as tk

class Apt:
    def __init__ (self):
        pass


    class gui:
    
        def __init__(self):
            
            self.root = tk.Tk()
            self.frame = tk.Frame(self.root)
            self.frame.pack()



            self.root.mainloop()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()



root.mainloop()