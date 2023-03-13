#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk

# from tkinter import ttk


class MyEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        if not "textvariable" in kw:
            self.variable = tk.StringVar()
            self.config(textvariable=self.variable)
        else:
            self.variable = kw["textvariable"]

    @property
    def value(self):
        return self.variable.get()

    @value.setter
    def value(self, new: str):
        self.variable.set(new)



class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Foo"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="tkGraf")
        self.lbl.pack()

        #! Výběr souboru
        self.fileFrame = tk.LabelFrame(self, text='Soubor')
        self.fileFrame.pack(padx=5, pady=5)
        self.fileEntry = MyEntry(self.fileFrame)
        self.fileEntry.pack()
        self.fileBtn = tk.Button(self.fileFrame, text='...')
        self.fileBtn.pack(anchor='e')
        
        #! Výběr formátu grafu
        self.dataformatVar = tk.IntVar() # Data pro RadioButton
        self.radkyRbtn = tk.Radiobutton(self.fileFrame,text="Data jsou ve sloupcích", variable=self.dataformatVar, value=0)
        self.radkyRbtn.pack(anchor='w')
        self.sloupceRbtn = tk.Radiobutton(self.fileFrame, text="Data jsou ve sloupcích", variable=self.dataformatVar, value=1)
        self.sloupceRbtn.pack(anchor='w')

        #! Tlačítko quit
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()