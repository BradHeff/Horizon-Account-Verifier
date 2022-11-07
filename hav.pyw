import threading
import GUI
import tkinter as tk
from tkinter import ttk
import Functions


class HAV(tk.Tk):
    """docstring for HAV."""

    def __init__(self):
        super(HAV, self).__init__()
        
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

        # self.bind("<Configure>", self.resize)

    # def resize(self, ass):
    #     self.lbl_error['text'] = str(self.winfo_height())

    def studentSearch(self, *args):

        if self.student_box.get().__len__() > 1:
            self.clearList()
            self.button_search['state'] = tk.DISABLED
            t = threading.Thread(target=self.search, args=(
                self.student_box.get(),))
            t.daemon = True
            t.start()
        else:
            self.lbl_error['text'] = "Search Not Valid!"
            self.lbl_error.configure(foreground='red')

    def clearList(self):
        self.tree.delete(*self.tree.get_children())

    def textChange(self, key):
        self.lbl_error['text'] = ""

    def search(self, name):
        self.prog['value'] = 20
        userList = Functions.findUser(self, name)
        self.prog['value'] = 60
        count = 0
        if userList.__len__() < 1:
            self.lbl_error['text'] = "Nothing Found!"
            self.lbl_error.configure(foreground='red')
        else:
            for x in userList:
                self.tree.tag_configure(
                    tagname="Disabled", background="#ff0000")
                self.tree.insert('', 'end', tags=userList[x]['status'], values=(
                    userList[x]['name'], userList[x]['email'], userList[x]['title'], userList[x]['status']))

                count += 1
                # print(count/userList.__len__())
                self.prog['value'] = (
                    count/userList.__len__())*100
            self.lbl_error['text'] = ''.join(
                ["Search Returned (", str(count), ") Results"])
            self.lbl_error.configure(foreground='green')
        self.student_box.delete(0, "end")
        self.button_search['state'] = tk.NORMAL
        self.prog['value'] = 0


if __name__ == '__main__':
    app = HAV()
    app.mainloop()
