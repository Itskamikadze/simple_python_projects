#Timer with Tkinter

#necesarry libs.
import time
import winsound
from tkinter import *

#shape of Timer
clock = Tk()
clock.geometry("400x600")
clock.title("Timer")
clock.config(bg="#000")
clock.maxsize(1000, 400)



#current time
def current_time():
    curr_t = time.strftime("%H:%M:%S %p")
    clock.after(1000, current_time)
    showtime.config(text=curr_t)

# timer countdown with sound when the time == 0
def timer():
    times = int(h.get())*3600 + int(m.get())*60 + int(s.get())
    while times > -1:
        minute, second = (times//60, times%60)
        hour = 0
        if minute > 60:
            hour, minute = (minute//60, minute%60)
        s.set(second)
        m.set(minute)
        h.set(hour)

        clock.update()
        time.sleep(1)

        if times == 0:
            winsound.PlaySound("C:\Windows\Media\Alarm05", winsound.SND_ASYNC)
            s.set("00")
            m.set("00")
            h.set("00")
        times -= 1
    

# variables (hour, min, sec)
h = StringVar()
Entry(clock, textvariable=h, width=2, font="arial 50", fg="#fff", background="#000", bd=0).place(x=30, y=155)
h.set("00")
m = StringVar()
Entry(clock, textvariable=m, width=2, font="arial 50", fg="#fff", background="#000", bd=0).place(x=150, y=155)
m.set("00")
s = StringVar()
Entry(clock, textvariable=s, width=2, font="arial 50", fg="#fff", background="#000", bd=0).place(x=270, y=155)
s.set("00")

Label(clock, text="hours", font="arial 12", bg="#000", fg="#fff").place(x=105, y=200)
Label(clock, text="mins", font="arial 12", bg="#000", fg="#fff").place(x=225, y=200)
Label(clock, text="secs", font="arial 12", bg="#000", fg="#fff").place(x=345, y=200)

# start button to start countdown
buttonStart = Button(clock, text="START", bg="green", fg="#fff", width=15, height=2, font="arial 10 bold", command=timer)
buttonStart.pack(padx=5, pady=5, side=LEFT)
buttonStart.place(x=30, y=300)
# stop button to stop program
buttonStop = Button(clock, text="STOP", bg="red", fg="#fff", width=15, height=2, font="arial 10 bold", command=clock.destroy)
buttonStop.pack(padx=5, pady=5, side=RIGHT)
buttonStop.place(x=240, y=300)


# show the current time
showtime = Label(clock, text="", fg="green", bg="black", font=("Helvetica", 48),)
showtime.pack(pady=20)
current_time()

#execute the program
clock.mainloop()


