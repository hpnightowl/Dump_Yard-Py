from tkinter import *
from PIL import Image,ImageTk
w=Tk()
w.geometry("500x500")
w.title("Form")
fn = StringVar()
ln = StringVar()
fb = StringVar()
#heading
head = Label(w,text="Feedback Form",relief="solid",width=20,font=("arial",19,"bold")).place(x=90,y=53)
#firstname
fn = Label(w,text="First Name : ",width=20,font=("arial",10,"bold")).place(x=60,y=140)
#lastname
ln = Label(w,text="Last Name : ",width=20,font=("arial",10,"bold")).place(x=60,y= 200)
#comments
com=Label(w,text="Comments",width=20,font=("arial",10,"bold")).place(x=170,y=240)
#button
done = Button(w,text="Done",width=5,bg="red",font=("arial",0,"bold")).place(x=400,y=420)
#Boxes
fnbox = Entry(w,textvar=fn).place(x=200,y=140)
lnbox = Entry(w,textvar=ln).place(x=200,y=200)
fbbox = Entry(w,textvar=fb,width=50).place(x=60,y=270)

w.mainloop()
