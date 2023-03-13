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

    #* Výběr souboru - FRAME
        self.fileFrame = tk.LabelFrame(self, text='Soubor')
        self.fileFrame.pack(padx=5, pady=5)
        self.fileEntry = MyEntry(self.fileFrame)
        self.fileEntry.pack()
        self.fileBtn = tk.Button(self.fileFrame, text='...')
        self.fileBtn.pack(anchor='e')
        
        #! Výběr formátu grafu
        self.dataformatVar = tk.IntVar() # Data pro RadioButton
        self.radkyRbtn = tk.Radiobutton(self.fileFrame,text="Data jsou v řádcích", variable=self.dataformatVar, value=0)
        self.radkyRbtn.pack(anchor='w')
        self.sloupceRbtn = tk.Radiobutton(self.fileFrame, text="Data jsou ve sloupcích", variable=self.dataformatVar, value=1)
        self.sloupceRbtn.pack(anchor='w')

        #! Tlačítko quit
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack

    #* Nastavení parametrů grafu - FRAME
        self.grafFrame = tk.LabelFrame(self, text='Parametry grafu')
        self.grafFrame.pack(padx=5, pady=5)

        # Nastavení titulku grafu
        tk.Label(self.grafFrame, text='Titulek').grid(row=0, column=0)
        self.titleEntry = MyEntry(self.grafFrame)
        self.titleENtry.grid(row=0, column=1)

        # Nastavení popisku osy x
        tk.Label(self.grafFrame, text='popisek X').grid(row=1, column=0)
        self.xlabelEntry = MyEntry(self.grafFrame)
        self.xlabelEntry.grid(row=1, column=1)

        # Nastavení popisku osy y
        tk.Label(self.grafFrame, text='popisek Y').grid(row=2, column=0)
        self.ylabelEntry = MyEntry(self.grafFrame)
        self.ylabelEntry.grid(row=2, column=1)

        # Nastavení mřížky
        tk.Label(self.grafFrame, text='mřížka').grid(row=3, column=0)
        self.gridChck = tk.Checkbutton(self.grafFrame)
        self.gridChck.grid(row=3, column=1, sticky='w')

        # Nastavení aproximace
        tk.Label(self.grafFrame, text='aproximace').grid(row=4, column=0)   
        self.selectAproximation = tk.Checkbutton(self.grafFrame)
        self.selectAproximation.grid(row=4, column=1, sticky='w')

    #!Funkce na ukončení aplikace
    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()