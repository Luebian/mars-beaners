import time
from random import random
import matplotlib
matplotlib.use('TkAgg') # do this before importing pylab
import matplotlib.pyplot as plt
import sys

archivo = sys.argv[1]
f = open(archivo,'r')
cabecera = f.readline()

def animate():
#    global x, y1, y2, y3
    datos = f.readline().split(',')
    if len(datos) == 4:
        x.append(int(datos.pop(0)))
        y1.append(int(datos.pop(0)))
        y2.append(int(datos.pop(0)))
        y3.append(int(datos.pop(0)))
        ax.set_xlim(-1, x[-1] + 1)
        line1.set_xdata(x)
        line2.set_xdata(x)
        line3.set_xdata(x)
        line1.set_ydata(y1)
        line2.set_ydata(y2)
        line3.set_ydata(y3)
        fig.canvas.draw()
        fig.canvas.manager.window.after(100, animate)

fig = plt.figure()
ax = fig.add_subplot(111)
x = [0]
y1 = [0]
y2 = [0]
y3 = [0]
line1, = ax.plot(x, y1)
line2, = ax.plot(x, y2)
line3, = ax.plot(x, y3)

ax.set_ylim(-0.5, 25.5)

fig.canvas.manager.window.after(100, animate)
plt.show()


