from tkinter import *

# creating basic window
window = Tk()
window.geometry("500x500")  # size of the window width:- 500, height:- 375
window.resizable(0, 0)  # this prevents from resizing the window
window.title("TIC-TAC-TOE")

input_text = StringVar()

def btn_click(item):
    if item%2 != 0:
        ch = Label(window,text="X",fg = "red",bg = "white",font=("arial",50,"bold")).place(x=80,y=160)
    else:
        ch = Label(window,text="O",fg = "red",bg = "white",font=("arial",50,"bold")).place(x=220,y=160)


blank1 = Button(window, text=" ", fg="black", width=15, height=5, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(1)).place(x=40,y=150)

blank2 = Button(window, text=" ", fg="black", width=15, height=5, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(2)).place(x=180,y=150)

blank3 = Button(window, text=" ", fg="black", width=15, height=5, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(2)).place(x=320,y=150)

blank4 = Button(window, text=" ", fg="black", width=15, height=5, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(1)).place(x=40,y=250)

blank5 = Button(window, text=" ", fg="black", width=15, height=5, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(2)).place(x=180,y=250)

blank6 = Button(window, text=" ", fg="black", width=15, height=5, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(2)).place(x=320,y=250)

blank7 = Button(window, text=" ", fg="black", width=15, height=5, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(1)).place(x=40,y=350)

blank8 = Button(window, text=" ", fg="black", width=15, height=5, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(2)).place(x=180,y=350)

blank9 = Button(window, text=" ", fg="black", width=15, height=5, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(2)).place(x=320,y=350)

window.mainloop()
