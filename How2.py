from tkinter import*
from PIL import Image,ImageTk
import How1
def how2_fn():
    

    w=Tk()
    w.title("How it works")
    w.geometry("1350x690")

    def back_fn():
        w.destroy()
        How1.how1_fn()



    i=Image.open("How2.jpg").resize((1350,690))
    img=ImageTk.PhotoImage(i)
    my_lb=Label(image=img)
    my_lb.place(x=-2,y=-2)

    click_here=Button(w,text="back",font=("times",15,"bold"),bg="orange",fg="white",activebackground="#EB984E",width=8,height=1,border=0,command=back_fn)
    click_here.place(x=1200,y=630)


    w.mainloop()