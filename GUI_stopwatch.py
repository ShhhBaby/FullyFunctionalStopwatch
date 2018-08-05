from tkinter import *
import time

def pause():
    global count
    count = 1

def restart():
    global count

    count = 1
    t.set('00:00:00')
    count = 0


def timer():

    global count


    if count == 0:

        d = str(t.get())
        h, m, s = map(int, d.split(":"))

        if s < 59:
            s += 1
        elif s == 59:
            s = 0
            if m < 59:
                m += 1
            elif m == 59:
                m = 0
                h += 1
        if (h < 10):
            h = str(0) + str(h)
        else:
            h = str(h)
        if (m < 10):
            m = str(0) + str(m)
        else:
            m = str(m)
        if (s < 10):
            s = str(0) + str(s)
        else:
            s = str(s)
        d = h + ":" + m + ":" + s

        t.set(d)
        if count == 0:
            root.after(1000, timer)

        h = int(h)
        s = int(s)
        m = int(m)

def continual():
    global count
    count = 0
    timer()

global count
count = 0
root = Tk()
root.title("Varun's Stopwatch")
root.geometry("600x450")
root.resizable(False, False)
t = StringVar(root)
t.set("00:00:00")

lab = Label(root, textvariable=t, font ="courier 80 bold", bg = "magenta")
lb2 = Label(root, text = "Use the buttons below!", font = "courier 30 bold")

lb1 = Label(root, text = "It's Varun's Stopwatch!", font = "Impact 47 ",bg ="yellow",)
lb1.pack(fill = X)
button1 = Button(root, text="Start", command=continual, font="Times 12 bold")
button2 = Button(root, text="Pause", command=pause, font='Times 12 bold')
button3 = Button(root, text="Reset", command=restart, font='Times 12 bold')
button4 = Button(root, text = "Continue", command= continual, font = "Times 12 bold")
lab.pack( fill = X)
lb2.pack(fill= X)
button1.place(x=130, y=320)
button2.place(x=255, y=320)
button3.place(x=370, y=320)
button4.place(x= 245, y= 370)
root.mainloop()



