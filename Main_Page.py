from tkinter import*
from PIL import Image,ImageTk
import Menu_Page
w=Tk()
w.title("Real Time Project")
w.geometry("1350x690")

def submit():
    w.destroy()
    Menu_Page.menu_page_fun()

i=Image.open("Crypto.jpg").resize((1350,690))
img=ImageTk.PhotoImage(i)
my_lb=Label(image=img)
my_lb.place(x=-2,y=-2)

click_here=Button(w,text="Click Here",font=("times",15,"bold"),bg="orange",fg="white",activebackground="#EB984E",command=submit)
click_here.place(x=940,y=570)

w.mainloop()