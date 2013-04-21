import time
import numpy as np
from random import random
import matplotlib
matplotlib.use('TKAgg') # do this before importing pylab
import matplotlib.pyplot as plt


def animate():
    next = x[-1] + 1 #agarr el ultimo elemento del arreglo y le suma 1 a ese valor
    x.append(next)#agrega el valor de next despues del ultimo valor del elemento
    y.append(random())#agrega aleatoriamente
    #ax.set_xlim(-2, next + 1)
    # for i in xrange(len(A)):
    #     A[i].set_xlim(0,next + 1)
    #     B[i].set_xdata(x)
    #     B[i].set_xdata(y)
    plt.scatter(x,y)  
    ax.set_xlim(0, next / 2)
    bx.set_xlim(0, next + np.log(10))
    cx.set_xlim(0,next + 1)
    line.set_xdata(x)
    line.set_ydata(y)
    line1.set_xdata(x)
    line1.set_ydata(y)
    line2.set_xdata(x)
    line2.set_ydata(y)
    
    fig.canvas.draw()
    
    fig.canvas.manager.window.after(100, animate)
    

fig = plt.figure()

# for i in xrange(len(A)):
#     j=j+1
#     A[i].fig.add_subplot(j)
ax = fig.add_subplot(311)
bx = fig.add_subplot(312)
cx = fig.add_subplot(313)
x = [-1]
y = [0.5]
# for i in xrange(len(A)):
#     B[i],=A[i].plot(x,y)
#     A[i].set_ylim(0.0,1.0)
line, = ax.plot(x,y)
line1, = bx.plot(x,y)
line2, = cx.plot(x,y)
ax.set_ylim(0.0, 1.0)
bx.set_ylim(0.0, 1.0)
cx.set_ylim(0.0, 1.0)
#bx.set_ylim(0.001, 0.005)

fig.canvas.manager.window.after(100, animate)

ax.set_ylabel("Temperatura")
bx.set_ylabel("Oxigeno")
cx.set_xlabel("Tiempo")
cx.set_ylabel("Dioxido de Carbono")


plt.show()

# def file_check(): 
#     file = open("datos.csv","r")
#     line = file.readlines()
#     if not line:
#         return 0

# def abrir():
#     arch=open("datos.csv","r")
#     cabecera = arch.readline()
#     vector=[]
#     #print cabecera                                                                                                                                                                                               
#     for data in arch.readlines():
#         data=data.strip()
#         vector.append(data.split(","))
#     #for i in xrange(len(vector)):                                                                                                                                                                                
#     plt.plot(vector)
#     plt.show()
#     arch.close()

# if(file_check()):
#     abrir()
# else:
#     print "No contents"
