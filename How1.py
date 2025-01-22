from tkinter import*
from PIL import Image,ImageTk
import How2
import Menu_Page
def how1_fn():

    w=Tk()
    w.title("Real Time Project")
    w.geometry("1350x690")

    def how2_fun():
        w.destroy()
        How2.how2_fn()

    def back_fn():
        w.destroy()
        Menu_Page.menu_page_fun()

    i=Image.open("How.jpg").resize((1350,690))
    img=ImageTk.PhotoImage(i)
    my_lb=Label(image=img)
    my_lb.place(x=-2,y=-2)

    #Introduction
    hd_lb=Label(w,text="How it works",font=("times",24,"bold"),fg="#FDFEFE",bg="#FFA500")
    hd_lb.place(x=580,y=1)

    click_here=Button(w,text="Next",font=("times",15,"bold"),bg="orange",fg="white",activebackground="#EB984E",width=8,height=1,border=0,command=how2_fun)
    click_here.place(x=1200,y=630)

    click_here=Button(w,text="back",font=("times",15,"bold"),bg="orange",fg="white",activebackground="#EB984E",width=8,height=1,border=0,command=back_fn)
    click_here.place(x=50,y=630)

    w.mainloop()