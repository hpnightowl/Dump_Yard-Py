from tkinter import *

# creating basic window
window = Tk()
window.geometry("500x500")  # size of the window width:- 500, height:- 375
window.resizable(0, 0)  # this prevents from resizing the window
window.title("TIC-TAC-TOE")

input_text = StringVar()

def btn_click(x1,y1,item):
   if item%2 != 0:
        ch = Label(window,text="X",fg = "red",bg = "white",font=("arial",50,"bold")).place(x=x1+40,y=y1+8)
   else:
        ch = Label(window,text="O",fg = "red",bg = "white",font=("arial",50,"bold")).place(x=x1+40,y=y1+8)
       
chance = 1
blank1 = Button(window, text=" ", fg="black", width=15, height=5, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(40,150,chance)).place(x=40,y=150)
blank2 = Button(window, text=" ", fg="black", width=15, height=5, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(180,150,chance)).place(x=180,y=150)
blank3 = Button(window, text=" ", fg="black", width=15, height=5, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(320,150,chance)).place(x=320,y=150)
blank4 = Button(window, text=" ", fg="black", width=15, height=5, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(40,250,chance)).place(x=40,y=250)
blank5 = Button(window, text=" ", fg="black", width=15, height=5, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(180,250,chance)).place(x=180,y=250)
blank6 = Button(window, text=" ", fg="black", width=15, height=5, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(320,250,chance)).place(x=320,y=250)
blank7 = Button(window, text=" ", fg="black", width=15, height=5, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(40,350,chance)).place(x=40,y=350)
blank8 = Button(window, text=" ", fg="black", width=15, height=5, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(180,350,chance)).place(x=180,y=350)
blank9 = Button(window, text=" ", fg="black", width=15, height=5, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(320,350,chance)).place(x=320,y=350)
window.mainloop()
