import threading
import GUI
import tkinter as tk
from tkinter import ttk
import Functions
import sv_ttk


class HAV(tk.Tk):
    """docstring for HAV."""

    def __init__(self):
        super(HAV, self).__init__()
        self.W = 0
        self.H = 0
        self.lbl_error = tk.Label()
        self.button_search = tk.Button()
        self.student_box = tk.Entry()
        self.tree = ttk.Treeview()
        self.prog = ttk.Progressbar()
        
        GUI.HAVGui(self)

        self.company = ""
        self.server = ""
        self.username = ""
        self.password = ""
        self.ou = ""
        self.domainName = ""

        self.compFail = False
        self.servs = False

        
        Functions.getConfig(self, Functions.getSettings(self, "Settings"))

        if self.compFail == True:
            self.lbl_error['text'] = "Server config in Settings failed"
            self.lbl_error.configure(foreground='red')
            self.button_search['state'] = tk.DISABLED
            self.student_box['state'] = tk.DISABLED
        
        
        t = threading.Thread(target=self.load)
        t.daemon = True
        t.start()


    def load(self):
        try:
            res = Functions.check_connection(self)
            cnt = 1
            self.prog['maximum'] = res.__len__()
            for x in res:
                self.prog['value'] = cnt
                cnt+=1
            self.prog['value'] = 0
            self.student_box['state'] = tk.NORMAL
            self.button_search['state'] = tk.NORMAL
        except Exception as e:
            print(e)
            self.messageBox("ERROR", "Failed to connect to server")


    def studentSearch(self, *args):

        if self.student_box.get().__len__() > 1:
            self.clearList()
            self.button_search['state'] = tk.DISABLED
            self.student_box['state'] = tk.DISABLED
            self.prog['maximum'] = 100
            t = threading.Thread(target=self.search, args=(
                self.student_box.get(),))
            t.daemon = True
            t.start()
        else:
            self.lbl_error['text'] = "Search Not Valid!"
            self.lbl_error.configure(foreground='red')
            self.messageBox("ERROR", "Search is not valid!")

    def clearList(self):
        self.tree.delete(*self.tree.get_children())

    def textChange(self, key):
        self.lbl_error['text'] = ""

    def search(self, name):
        userList = Functions.findUser(self, name)        
        count = 1
        max = userList.__len__()
        
        if max < 1:
            self.lbl_error['text'] = "Nothing Found!"
            self.lbl_error.configure(foreground='red')
        else:
            for x in userList:
                self.tree.tag_configure(
                    tagname="Disabled", background="#ff0000")
                self.tree.insert('', 'end', tags=userList[x]['status'], values=(
                    userList[x]['name'], userList[x]['email'], userList[x]['title'], userList[x]['status']))

                count += 1
                self.prog['value'] = (
                    count/max)*100
            self.lbl_error['text'] = ''.join(
                ["Search Returned (", str(count), ") Results"])
            self.lbl_error.configure(foreground='green')
        
        self.student_box['state'] = tk.NORMAL
        self.student_box.delete(0, "end")
        self.button_search['state'] = tk.NORMAL
        self.prog['value'] = 0

    def messageBox(self, title, txt):
        ap = tk.Tk()
        geo = self.winfo_geometry()
        posX = geo.split("+")[1]
        posY = geo.split("+")[2]            
        
        center_x = int(int(posX) + (self.W/2) - 100)
        center_y = int(int(posY) + (self.H/2) - 25)
        
        try:
            sv_ttk.set_theme("dark")
        except Exception as e:
            print(e)        

        message = tk.Label(ap, text=txt)
        
        ap.title(title)
        ap.geometry(f'200x50+{center_x}+{center_y}')
        ap.attributes("-fullscreen", False)
        ap.attributes("-toolwindow", True)
        ap.attributes("-topmost", True)
        
        message.pack(fill='both',expand=True)
        
        ap.mainloop()


if __name__ == '__main__':
    app = HAV()
    app.mainloop()
