import time
import Tkinter as tk
import sys
from Tkinter import *
import os


#setting up the frame of the clock
root = Tk()
root.title("Sourcecodester")
width = 600
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2)- (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="light blue")
root.hasAlarmRung = False

#setting up the layout of the clock

Top = Frame(root, width=600, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(root, width=600)
Mid.pack(side=TOP, expand=1)


#===========================================LABEL WIDGET==================================
lbl_title = Label(Top, text="Python: Simple Digital Clock", width=600, font=("arial", 20))
lbl_title.pack(fill=X)

clock = Label(Mid, font=('times', 50 , 'bold'), fg="green", bg='pink')
clock.pack()

#creating the function of the clock
def tick(root):
    # setTime = time.strftime('%I: %M: %S %p')
    # clock.config(text=setTime )
    # clock.after(200, tick)
    setTime = time.strftime('%I:%M:%S %p')
    if "3:58" in setTime and root.hasAlarmRung == False:
        duration = 0.1  # millisecond
        freq = 440  # Hz
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
        clock.config(text=setTime)
        clock.after(200, tick)
        root.hasAlarmRung = True
    else:
        clock.config(text=setTime)
        clock.after(200, tick)
    return(setTime)



#initialising the clock

if __name__ == '__main__':
    tick(root)
    root.mainloop()
