from tkinter import *

w=Tk()
w.geometry("500x500")
w.title("To-do")

def newcheck():
    ch = Checkbutton(w).place(x=40,y=40)

heading = Label(w,text="hpnightowl-To-do",bg="yellow",fg="blue",font=("aerial",20,"bold")).pack()

add_button = Button(w,text="+",bg="red",font=("aerial",20,"bold"),command=newcheck()).place(x=410,y=410)


w.mainloop()
