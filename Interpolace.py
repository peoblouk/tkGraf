import scipy.interpolate as inp #https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.UnivariateSpline.html
import pylab as lab # grafy

x = "0 0.3 0.5 0.8 1 2 3".split()
y = "0 0.1 0.5 1   3 10 30".split()

x = list(map(float, x)) # funkce map předáme dva parametry a seznam
y = list(map(float, y))
''' 
# to je to samé jako funcke map
bagr= []
for cislo in x:
    bagr.append(float(x))
x = bagr
'''

newX = lab.linspace(0,3, 333)

# aproximace
# spl = inp.CubicSpline(x,y)
# spl = inp.LSQUnivariateSpline(x,y) # metoda nejmenších čtverců
spl = inp.UnivariateSpline(x,y) # apro
# spl = inp.BSpline(x,y, 3)
newY = spl(newX)

lab.plot(x,y,"o", label="měřící body")
lab.plot(newX, newY, ":", label="interpolace")
lab.grid(1)
lab.legend()
lab.show()