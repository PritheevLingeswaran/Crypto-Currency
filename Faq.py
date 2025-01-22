from tkinter import*
from PIL import Image,ImageTk
import Menu_Page
def faq_fn():
    
    w=Tk()
    w.title("How it works")
    w.geometry("1350x690")

    def back_fn():
        w.destroy()
        Menu_Page.menu_page_fun()
        
    i=Image.open("Faq.jpg").resize((1350,690))
    img=ImageTk.PhotoImage(i)
    my_lb=Label(image=img)
    my_lb.place(x=-2,y=-2)

    #FAQ
    hd_lb=Label(w,text="FAQ",font=("times",24,"bold"),fg="#FDFEFE",bg="#FFA500")
    hd_lb.place(x=662,y=1,)

    click_here=Button(w,text="back",font=("times",15,"bold"),bg="orange",fg="white",activebackground="#EB984E",width=8,height=1,border=0,command=back_fn)
    click_here.place(x=1200,y=640)

    w.mainloop()