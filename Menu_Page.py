from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import requests
import Introduction
import Use
import How1
import Faq
import Types
import Details
import Track

def menu_page_fun():
    
    w=Tk()
    w.title("Real Time Project")
    w.geometry("1350x690")
    def intro_fun():
        w.destroy()
        Introduction.introduction_fun()
    def use_fun():
        w.destroy()
        Use.use_fn()
    def how1_fun():
        w.destroy()
        How1.how1_fn()
    def faq_fun():
        w.destroy()
        Faq.faq_fn()
    def types_fun():
        w.destroy()
        Types.types_fn()
    def details_fun():
        w.destroy()
        Details.details_fn()
        
    def track_fun():
        w.destroy()
        Track.tr()



    
 
    i=Image.open("Menu.jpg").resize((1350,700))
    img=ImageTk.PhotoImage(i)
    my_lb=Label(image=img)
    my_lb.place(x=-2,y=-2)

    #Introduction
    in_ent=Button(w,text="Introduction",font=("Arial",16),bg="#FFA500",fg="white",activebackground="#FFA500",activeforeground="black",width=15,height=2,border=0,command=intro_fun)
    in_ent.place(x=250,y=3)
    
    #How to use
    ho_ent=Button(w,text="How to use",font=("Arial",16),bg="#FFA500",fg="white",activebackground="#FFA500",activeforeground="black",width=15,height=2,border=0,command=use_fun)
    ho_ent.place(x=450,y=3)

    #How it works
    pa_ent=Button(w,text="How it works",font=("Arial",16),bg="#FFA500",fg="white",activebackground="#FFA500",activeforeground="black",width=15,height=2,border=0,command=how1_fun)
    pa_ent.place(x=650,y=3)

    #FAQ
    fa_ent=Button(w,text="FAQ",font=("Arial",16),bg="#FFA500",fg="white",activebackground="#FFA500",activeforeground="black",width=15,height=2,border=0,command=faq_fun)
    fa_ent.place(x=850,y=3)

    #English
    en_label=Label(w,text="in English",font=("Arial",14),bg="#FFA500",fg="white",activebackground="#FFA500",activeforeground="black",width=15,height=2,border=0)
    en_label.place(x=1200,y=6)

    #Type of crypto
    ty_ent=Button(w,text="Types of Crypto Currencies",font=("Arial",16),bg="#FFA500",fg="white",activebackground="White",activeforeground="black",width=23,height=1,border=1,command=types_fun)
    ty_ent.place(x=180,y=370)

    #Buy and Sell Crypto Currencies
    by_ent=Button(w,text="Buy and Sell Crypto Currencies",font=("Arial",16),bg="#FFA500",fg="white",activebackground="White",activeforeground="black",width=27,height=1,border=1,command=details_fun)
    by_ent.place(x=500,y=370)

    #Tracker
    co_ent=Button(w,text="Crypto Currency Tracker",font=("Arial",16),bg="#FFA500",fg="white",activebackground="White",activeforeground="black",width=23,height=1,border=1,command=track_fun)
    co_ent.place(x=860,y=370)

    w.mainloop()