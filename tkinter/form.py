from tkinter import *

w=Tk()
w.geometry("500x500")
w.title("Form")

#heading
head = Label(w,text="Feedback Form",relief="solid",width=20,font=("arial",19,"bold")).place(x=90,y=53)
#firstname
fn = Label(w,text="First Name",width=20,font=("arial",10,"bold")).place(x=60,y=140)
#lastname
ln = Label(w,text="Last Name",width=20,font=("arial",10,"bold")).place(x=60,y= 200)

done = Button(w,text="Done",width=5,bg="red",font=("arial",0,"bold")).place(x=400,y=420)
w.mainloop()
