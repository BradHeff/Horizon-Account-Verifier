import tkinter as tk
from tkinter import ttk
from Functions import Version, Title
from Image_Date import image

print(Version[5])


def Window(self):
    W, H = 715, 200
    self.title(''.join([Title, ' ', Version[0:2], '.',
               Version[Version.__len__()-1]]))
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    center_x = int(screen_width/2 - W / 2)
    center_y = int(screen_height/2 - H / 2)
    self.geometry(f'{W}x{H}+{center_x}+{center_y}')
    self.resizable(0, 0)
    self.attributes("-fullscreen", False)


def Icon(self):
    photo = tk.PhotoImage(data=image)
    self.wm_iconphoto(False, photo)


def HAVGui(self):
    Window(self)
    Icon(self)
    style = ttk.Style()
    style.theme_use("xpnative")
    style.map("Treeview")

    paddings = {'padx': 2, 'pady': 15}
    entry_font = {'font': ('Helvetica', 11)}

    frm1 = tk.Frame(self)
    frm2 = tk.Frame(self)

    self.lbl_title = ttk.Label(self, text="Horizon Christian School Account Verifier")
    self.lbl_title.grid(columnspan=4, row=0, sticky='N', padx=10, pady=10)

    lbl_year = ttk.Label(frm1, text="Year Level: ")
    lbl_year.grid(column=0, row=1, sticky='W', **paddings)

    self.year_val = tk.StringVar(frm1, 'Select Year')
    self.year_box = ttk.Combobox(frm1, textvariable=self.year_val, width=40)
    self.year_box['state'] = 'readonly'
    self.year_box['values'] = ['self.accountSubjects']
    self.year_box.set("Select Year")
    self.year_box.bind('<<ComboboxSelected>>', self.yearSelect)
    self.year_box.grid(column=1, row=1, sticky='E', **paddings)

    lbl_account = ttk.Label(frm2, text="Year Level: ")
    lbl_account.grid(column=2, row=1, sticky='W', **paddings)

    self.account_val = tk.StringVar(frm2, 'Select Student')
    self.account_box = ttk.Combobox(
        frm2, textvariable=self.account_val, width=40)
    self.account_box['state'] = 'readonly'
    self.account_box['values'] = ['self.accountSubjects']
    self.account_box.set("Select Student")
    self.account_box.bind('<<ComboboxSelected>>', self.yearSelect)
    self.account_box.grid(column=3, row=1, sticky='EW', **paddings)

    frm1.grid(column=0, row=1, padx=10, pady=5)
    frm2.grid(column=1, row=1, padx=10, pady=5)
