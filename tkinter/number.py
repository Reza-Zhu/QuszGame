import tkinter as tk
import tkinter.messagebox
import random
var1=0
window = tk.Tk()
window.title('Guess Number')
window.geometry('400x100')
answer=random.randint(0,10)
e = tk.Entry(window, show=None)
e.pack()

def insert_point():
    global var1
    var1.set(var1.get()+1)
    var = int(e.get())
    if var>answer:
        tkinter.messagebox.showinfo(title='Error',
                                    message='too big')
    if var==answer:
        tkinter.messagebox.showinfo(title='Correct',
                                    message='wonderful')
    if var<answer:
        tkinter.messagebox.showinfo(title='Error',
                                    message='too small')

b1 = tk.Button(window, text='insert point', width=15,
              height=2, command=insert_point)
b1.pack()
var1=tk.IntVar()
l1= tk.Label(window,textvariable=var1)
l1.pack()
l2=tk.Label(window,text='You have tried: ')
l2.place(x=100,y=68)
l2=tk.Label(window,text='times')
l2.place(x=205,y=68)
window.mainloop()