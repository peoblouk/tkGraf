import scipy.interpolate as inp
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
newX = lab.linspace(0,3, 33)
spl = inp.CubicSpline(x,y)
newY = spl(newX)

lab.plot(x,y,"o", label="měřící body")
lab.plot(newX, newY, "x", label="interpolace")
lab.grid(1)
lab.legend()
lab.show()