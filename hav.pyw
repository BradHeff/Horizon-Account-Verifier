import threading
import GUI
import tkinter as tk
import Functions


class HAV(tk.Tk):
    """docstring for HAV."""

    def __init__(self):
        super(HAV, self).__init__()
        GUI.HAVGui(self)

        self.server = ""
        self.username = ""
        self.password = ""
        self.ou = ""
        self.domainName = ""

        self.compFail = False
        self.servs = False

        Functions.getConfig(self, "DComputers")

        if self.compFail == True:
            # type: ignore
            self.lbl_error['text'] = "Server config in Settings failed"  # type: ignore
            self.lbl_error.configure(foreground='red')  # type: ignore
            self.button_search['state'] = tk.DISABLED  # type: ignore
            self.student_box['state'] = tk.DISABLED  # type: ignore

        # self.bind("<Configure>", self.resize)

    # def resize(self, ass):
    #     self.lbl_error['text'] = str(self.winfo_height()) # type: ignore

    def studentSearch(self, *args):

        if self.student_box.get().__len__() > 1:  # type: ignore
            self.clearList()
            self.button_search['state'] = tk.DISABLED  # type: ignore
            t = threading.Thread(target=self.search, args=(
                self.student_box.get(),))  # type: ignore
            t.daemon = True
            t.start()
        else:
            self.lbl_error['text'] = "Search Not Valid!"  # type: ignore
            self.lbl_error.configure(foreground='red')  # type: ignore

    def clearList(self):
        self.tree.delete(*self.tree.get_children())  # type: ignore

    def textChange(self, key):
        self.lbl_error['text'] = ""  # type: ignore

    def search(self, name):
        self.prog['value'] = 20  # type: ignore
        userList = Functions.findUser(self, name)
        self.prog['value'] = 60  # type: ignore
        count = 0
        if userList.__len__() < 1:
            self.lbl_error['text'] = "Nothing Found!"  # type: ignore
            self.lbl_error.configure(foreground='red')  # type: ignore
        else:
            for x in userList:
                self.tree.insert('', 'end', values=(  # type: ignore
                    userList[x]['name'], userList[x]['email'], userList[x]['title']))  # type: ignore
                count += 1
                # print(count/userList.__len__())
                self.prog['value'] = (count/userList.__len__())*100  # type: ignore
            self.lbl_error['text'] = ''.join(  # type: ignore
                ["Search Returned (", str(count), ") Results"])  # type: ignore
            self.lbl_error.configure(foreground='green')  # type: ignore        
        self.student_box.delete(0, "end")  # type: ignore
        self.button_search['state'] = tk.NORMAL  # type: ignore
        self.prog['value'] = 0  # type: ignore


if __name__ == '__main__':
    app = HAV()
    app.mainloop()
