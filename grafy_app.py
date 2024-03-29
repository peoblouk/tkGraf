#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import filedialog # prohlížeč souborů
from tkinter import Menu
import pylab as pl # grafy
import scipy.interpolate as inp #https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.UnivariateSpline.html

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

    #* Main menu
        self.mainMenu = tk.Menu(self)
        self.mainMenu.add_command(label='O aplikaci')
        self.mainMenu.add_separator()
        self.mainMenu.add_command(label='Quit', command=self.quit, accelerator='ALT+F4')

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

    #* Nastavení parametrů grafu - FRAME
        self.grafFrame = tk.LabelFrame(self, text='Parametry grafu')
        self.grafFrame.pack(padx=5, pady=5)

        # Nastavení titulku grafu
        tk.Label(self.grafFrame, text='Titulek').grid(row=0, column=0)
        self.titleEntry = MyEntry(self.grafFrame)
        self.titleEntry.grid(row=0, column=1, columnspan=2)

        # Nastavení popisku osy x
        tk.Label(self.grafFrame, text='popisek X').grid(row=1, column=0)
        self.xlabelEntry = MyEntry(self.grafFrame)
        self.xlabelEntry.grid(row=1, column=1, columnspan=2)

        # Nastavení popisku osy y
        tk.Label(self.grafFrame, text='popisek Y').grid(row=2, column=0)
        self.ylabelEntry = MyEntry(self.grafFrame)
        self.ylabelEntry.grid(row=2, column=1, columnspan=2)

        # Nastavení mřížky
        self.gridVar = tk.BooleanVar(value=False)
        tk.Label(self.grafFrame, text='mřížka').grid(row=3, column=0)
        self.gridChck = tk.Checkbutton(self.grafFrame, variable=self.gridVar)
        self.gridChck.grid(row=3, column=1, sticky='w')

        # Nastavení stylu čáry
        self.lineVar = tk.StringVar(value='None')
        tk.Label(self.grafFrame, text='styl čáry').grid(row=4, column=0)
        self.lineOpt = tk.OptionMenu(self.grafFrame, self.lineVar, 'None', '-', ':', '--', '-.')
        self.lineOpt.grid(row=4, column=1, sticky='w')

        # Nastaveni bodů
        self.markerVar = tk.StringVar(value='None')
        tk.Label(self.grafFrame, text='styl marker').grid(row=5, column=0)
        self.markerOpt = tk.OptionMenu(self.grafFrame, self.markerVar, 'None', *tuple(',.oxX+*P123<>v^D'))
        self.markerOpt.grid(row=5, column=1, sticky='w')

        # Nastavení barvy čáry
        self.colorVar = tk.StringVar(value='black')
        tk.Label(self.grafFrame, text='barva čáry').grid(row=6, column=0)
        self.colorOpt = tk.OptionMenu(self.grafFrame, self.colorVar, "Black","Green", "Red", "Blue", "Purple", "Pink", "Yellow", "Grey", "Orange")
        self.colorOpt.grid(row=6, column=1, sticky='w')

        # Nastavení barvy markerů
        self.mcolorVar =tk.StringVar(value='black')
        tk.Label(self.grafFrame, text='barva marker').grid(row=7, column=0)
        self.markerOpt = tk.OptionMenu(self.grafFrame, self.mcolorVar, "Black","Green", "Red", "Blue", "Purple", "Pink", "Yellow", "Grey", "Orange")
        self.markerOpt.grid(row=7, column=1, sticky='w')

        # Nastavení aproximace
        self.aproxVar = tk.BooleanVar(value=False)
        tk.Label(self.grafFrame, text='aproximace').grid(row=8, column=0)   
        self.selectAproximation = tk.Checkbutton(self.grafFrame, variable=self.aproxVar)
        self.selectAproximation.grid(row=8, column=1, sticky='w')

        #! Tlačítko kreslit
        tk.Button(self, text='Kreslit', command=self.plotGraph).pack(anchor='w')

        #! Tlačítko quit
        tk.Button(self, text='Quit', command=self.quit).pack(anchor='e')

    #! Funkce na select souboru
    def fileSelect(self, event=None):
        self.filename = tk.filedialog.askopenfilename()
        self.fileEntry.value = self.filename

    def plotGraph(self):
        with open(self.filename, 'r') as f:
            if self.dataformatVar.get() == 0: #? data jsou v řádcích
                x = f.readline().split(';')
                y = f.readline().split(';')
                x = [float(i.replace(',', '.')) for i in x]
                y = [float(i.replace(',', '.')) for i in y]

            elif self.dataformatVar.get() == 1: #? data jsou ve sloupcích
                x = []
                y = []
                while True:
                    line = f.readline()
                    if line == '':
                        break
                    x1, y1 = line.split(';')
                    x1 = (float(x1.replace(',', '.')))   
                    y1 = (float(y1.replace(',', '.')))   
                    x.append(x1)
                    y.append(y1)
            if self.aproxVar == True: # nastavení aproximace
                newX = pl.linspace(0,3, 333)
                # aproximace
                # spl = inp.CubicSpline(x,y)
                spl = inp.LSQUnivariateSpline(x,y) # metoda nejmenších čtverců
                # spl = inp.UnivariateSpline(x,y) # apro
                # spl = inp.BSpline(x,y, 3)
                newY = spl(newX)
                self
            elif self.aproxVar == False: # nastavení aproximace
                pass
        pl.plot(x,y,'o',marker=self.markerVar.get(),linestyle=self.lineVar.get(),color=self.colorVar.get(), markeredgecolor=self.mcolorVar.get())
        pl.title(self.titleEntry.value)
        pl.xlabel(self.xlabelEntry.value)
        pl.ylabel(self.ylabelEntry.value)
        pl.grid(self.gridVar.get())
        pl.show()

    #!Funkce na ukončení aplikace
    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()