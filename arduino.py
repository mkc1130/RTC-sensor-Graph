from tkinter.constants import Y
import matplotlib
import serial
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import time



arduino = serial.Serial('/dev/cu.usbserial-A10K5326', 115200)
matplotlib.rcParams['font.family'] = 'AppleGothic'
fig = plt.figure(figsize=(18, 8))
ax = plt.axes(xlim=(0, 10), ylim=(0, 100))
max_points = 100
line, = ax.plot(np.arange(max_points), 
                np.ones(max_points, dtype=np.float64)*np.nan, label = '온도', color = 'r', linewidth=1)
# line1, = ax.plot(np.arange(max_points), 
#                 np.ones(max_points, dtype=np.float64)*np.nan, label = '습도', color = 'g', linewidth=1)
# line2, = ax.plot(np.arange(max_points), 
#                 np.ones(max_points, dtype=np.float64)*np.nan, label = '토양 습도', color = 'brown', linewidth=1)
ax.legend(loc=(0.8, 1), fontsize=12)
global timte_t
time_t = ['','','','','','','','','']
global y
def init():
    return line,
# def init1():
#     return line1,
# def init2():
#     return line2,

def animate(i):
    global time_t
    global y
    y = arduino.readline()
    y = y.decode()[0:-2]
    y = y.split(",")
    y0 = float(y[0])
    
    old_y = line.get_ydata()
    new_y = np.r_[old_y[1:], y0]
    line.set_ydata(new_y)
    
    
    tm = time.localtime(time.time())
    time_t.append(time.strftime('%I:%M:%S', tm))
    plt.xticks(np.arange(0,10),time_t)
    time_t = time_t[1:]
    return line,
# def animate1(i):
#     global time_t
#     y1 = arduino.readline()
#     y1 = y1.decode()[0:-2]
#     y1 = y1.split(",")
#     y1 = float(y1[1])
    
#     old_y1 = line1.get_ydata()
#     new_y1 = np.r_[old_y1[1:], y1]
#     line1.set_ydata(new_y1)
#     return line1,
# def animate2(i):
#     global time_t
#     y2 = arduino.readline()
#     y2 = y2.decode()[0:-2]
#     y2 = y2.split(",")
#     y2 = float(y2[2])
    
#     old_y2 = line2.get_ydata()
#     new_y2 = np.r_[old_y2[1:], y2]
#     line2.set_ydata(new_y2)
#     return line2,
    

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=1000, blit=False)
# anim1 = animation.FuncAnimation(fig, animate1, init_func=init1, frames=200, interval=1000, blit=False)
# anim2 = animation.FuncAnimation(fig, animate2, init_func=init2, frames=200, interval=1000, blit=False)

plt.show()