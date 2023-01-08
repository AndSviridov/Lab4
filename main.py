from tkinter import *
from tkinter.ttk import Progressbar as Pbr
from keygen import key
from threading import Thread
from time import sleep
from random import randint
from playsound import playsound

bar_prog = 0

def key_message():
    global message
    message = Tk()
    message.title('key')
    message.geometry('320x60')
    message.resizable(width=False, height=False)

    text = Text(message, height=1, font="Sylfaen 12")
    text.insert("end", key())
    text.configure(state="disabled")
    text.pack()

    cl1_btn = Button(message, text='ОК', command=close)
    cl1_btn.place(x=250, y=43, anchor=CENTER)
    cl2_btn = Button(message, text='Ладно', command=close)
    cl2_btn.place(x=290, y=43, anchor=CENTER)
    message.mainloop()

def close():
    message.destroy()
    window.destroy()

def progress():
    global bar_prog
    bar_prog = 0
    a = 0.05
    while bar_prog <= 100:
        bar_prog = bar_prog + 1
        bar['value'] = bar_prog
        a = a + randint(-1, 1)/20
        sleep(max(0.01, a))
    key_message()

def click():
    sound_th.start()
    bar()
    bar_th.start()

def sound():
        playsound('soundtrack.mp3')

def bar():
    global bar, window
    bar = Pbr(window, length=300)
    bar.place(x=320, y=290, anchor=CENTER)


bar_th = Thread(target=progress, daemon=True)
sound_th = Thread(target=sound, daemon=True)

window = Tk()
window.title('Джедай: Падший Орден KeyGen')
window.geometry('640x360')
window.resizable(width=False, height=False)

bg = PhotoImage(file='background.png')
bg_label = Label(window, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

gen_btn = Button(window, text='Сгенерировать ключ', command=click)
gen_btn.place(x=320, y=330, anchor=CENTER)

window.mainloop()
