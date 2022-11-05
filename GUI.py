import tkinter as tk
from tkinter import ttk
from Functions import Version, Title
from Image_Date import image
import sv_ttk

def Window(self):
    W, H = 650, 400
    self.title(''.join([Title, ' ', Version[0:2], '.',
               Version[Version.__len__()-1]]))
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    center_x = int(screen_width/2 - W / 2)
    center_y = int(screen_height/2 - H / 2)
    self.geometry(f'{W}x{H}+{center_x}+{center_y}')
    # self.resizable(0, 0)
    self.attributes("-fullscreen", False)


def Icon(self):
    photo = tk.PhotoImage(data=image)
    self.wm_iconphoto(False, photo)


def HAVGui(self):
    Window(self)
    Icon(self)
    
    sv_ttk.set_theme("dark")
    # style = ttk.Style()
    # style.theme_use(themename="classic")
    # style.map("Treeview")

    paddings = {'padx': 2, 'pady': 15}
    entry_font = {'font': ('Helvetica', 11)}
    self.rowconfigure(4, weight=2)
    frm1 = tk.Frame(self)
    frm1.columnconfigure(1, weight=2)
    frm2 = tk.Frame(self)

    self.lbl_title = ttk.Label(
        self, text="Horizon Christian School Account Verifier")
    self.lbl_title.grid(columnspan=4, row=0, sticky='N', padx=10, pady=10)

    lbl_name = ttk.Label(frm1, text="Enter Student Name: ")
    lbl_name.grid(column=0, row=0, sticky=tk.NS, **paddings)

    self.student_box = tk.Entry(frm1, width=48)
    self.student_box.bind_all('<KeyPress>', self.textChange)
    self.student_box.bind("<Return>", self.studentSearch)
    self.student_box.grid(column=1, columnspan=2, row=0,
                          sticky=tk.EW, **paddings)

    self.button_search = tk.Button(
        frm2, text="Search...", command=self.studentSearch, width=20)
    self.button_search.grid(column=0, row=0, sticky=tk.E, **paddings)

    frm1.grid(columnspan=2, row=1, padx=5, pady=0)
    frm2.grid(column=3, row=1, padx=5, pady=0)

    frame = tk.Frame(self)

    self.tree = ttk.Treeview(frame, columns=(
        "c1", "c2", "c3"), show='headings')

    scrollbar = tk.Scrollbar(frame)
    scrollbar.config(command=self.tree.yview)
    scrollbar.pack(side="right", fill="y")

    self.tree.config(yscrollcommand=scrollbar.set)

    self.tree.column("# 1", anchor=tk.CENTER)
    self.tree.heading("# 1", text="NAME")
    self.tree.column("# 2", anchor=tk.CENTER)
    self.tree.heading("# 2", text="EMAIL")
    self.tree.column("# 3", anchor=tk.CENTER)
    self.tree.heading("# 3", text="TITLE")

    self.tree.pack(side='left', fill='x')

    self.lbl_error = tk.Label(self, text="", font="Helvetica 13 bold")
    self.lbl_error.configure(foreground='red')
    self.lbl_error.grid(sticky=tk.W, column=0, row=2, padx=10)
    frame.grid(sticky=tk.NSEW, columnspan=4, row=3, padx=10)
    
    self.prog = ttk.Progressbar(self, orient=tk.HORIZONTAL, mode="determinate", maximum=100, length=630)
    self.prog.grid(sticky=tk.S, columnspan=4, row=4, **paddings)
    