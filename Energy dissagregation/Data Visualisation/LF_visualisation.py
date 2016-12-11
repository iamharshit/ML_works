import matplotlib.pyplot as plt
import numpy as np
import time
import csv

plt.ion()

#Setting constants
min_x = 0
max_x = 400

figure, ax = plt.subplots()
lines, = ax.plot([],[], 'k')

ax.set_autoscaley_on(True)
ax.set_xlim(min_x, max_x)
ax.grid()

def on_running(xdata, ydata):
    lines.set_xdata(xdata)
    lines.set_ydata(ydata)
    
    ax.relim()
    ax.autoscale_view()
    
    figure.canvas.draw()
    figure.canvas.flush_events()

xdata = np.array([60, 120, 180, 240, 300, 360])
y = np.genfromtxt('LF1P.csv', delimiter=',',dtype=np.float_)
y2 = np.genfromtxt('TimeTicks1.csv', delimiter=',',dtype=np.int)

ydata = []
for i in range(330000,y.shape[0],100):
    ydata = y[i]   
    print y[i][0], '  time= ',y2[i]
    #print ydata
    on_running(xdata, ydata)
    time.sleep(0.1)