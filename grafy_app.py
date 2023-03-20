#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import filedialog # prohlížeč souborů
import pylab as lab # grafy

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
        self.fileFrame.pack(padx=5, pady=5, fill='x') # fill je roztažení ve směru osy x
        self.fileEntry = MyEntry(self.fileFrame)
        self.fileEntry.pack(fill='x')
        self.fileBtn = tk.Button(self.fileFrame, text='...', command=self.fileSelect)
        self.fileBtn.pack(anchor='e')
        
        #! Výběr formátu grafu
        self.dataformatVar = tk.IntVar() # Data pro RadioButton
        self.radkyRbtn = tk.Radiobutton(self.fileFrame,text="Data jsou v řádcích", variable=self.dataformatVar, value=0)
        self.radkyRbtn.pack(anchor='w')
        self.sloupceRbtn = tk.Radiobutton(self.fileFrame, text="Data jsou ve sloupcích", variable=self.dataformatVar, value=1)
        self.sloupceRbtn.pack(anchor='w')

        #! Tlačítko kreslit
        tk.Button(self, text='Kreslit', command=self.plotGraph).pack(anchor='w')

        #! Tlačítko quit
        tk.Button(self, text='Quit', command=self.quit).pack(anchor='e')

    #* Nastavení parametrů grafu - FRAME
        self.grafFrame = tk.LabelFrame(self, text='Parametry grafu')
        self.grafFrame.pack(padx=5, pady=5)

        # Nastavení titulku grafu
        tk.Label(self.grafFrame, text='Titulek').grid(row=0, column=0)
        self.titleEntry = MyEntry(self.grafFrame)
        self.titleEntry.grid(row=0, column=1)

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

    #! Funkce na select souboru
    def fileSelect(self, event=None):
        self.filename = tk.filedialog.askopenfilename()
        self.fileEntry.value = self.filename

    def plotGraph(self):
        with open(self.filename, 'r') as f:
            if self.dataformatVar.get() == 1: #? data jsou ve sloupcích 
                x = f.readline().split(';')
                y = f.readline().split(';')
                x = [float(i.replace(',', '.')) for i in x]
                y = [float(i.replace(',', '.')) for i in y]

            elif self.dataformatVar.get() == 1: #? data jsou v řádcích
                pass
        lab.plot(x,y,'o')
        lab.show()

    #!Funkce na ukončení aplikace
    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()