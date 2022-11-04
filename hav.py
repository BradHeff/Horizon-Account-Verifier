import GUI
import tkinter as tk
from tkinter import ttk


class HAV(tk.Tk):
    """docstring for HAV."""
    def __init__(self):
        super(HAV, self).__init__()        
        GUI.HAVGui(self)
        # self.bind("<Configure>", self.resize)

    def yearSelect(self, subject):
        pass
    
    # def resize(self, some):
    #     self.lbl_title['text'] = ''.join(["Horizon Christian School Account Verifiers",str(self.winfo_width())])
        
if __name__ == '__main__':
    app = HAV()
    app.mainloop()
