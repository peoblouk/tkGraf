import pylab as pl
from numpy import pi

f = 50

t = pl.linspace(0,0.1, 333)

u = 3.3 * pl.cos(2*pi*f*t)
i = 1.1 * pl.cos(2*pi*f*t + pi/4)

p = u * i

pl.figure(1)
pl.plot(t, u, label = 'u') # label je parametr pro legendu
pl.plot(t, i, label = 'i')
pl.plot(t, p, label = 'p')
pl.grid(True)
pl.legend(loc='upper right')

pl.xlim([0,0.2]) # Nastuvuje vykreslení od do
pl.title('Výkon střídavého proudu')
pl.xlabel('t [s]')
pl.ylabel('u(t), i(t), p(t)')

pl.show()