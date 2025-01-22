from tkinter import*
from PIL import Image,ImageTk
import Buy
import Menu_Page
def details_fn():

    w=Tk()
    w.title("Real Time Project")
    w.geometry("1350x690")

    def buy_fun():
        w.destroy()
        Buy.buy_fn()

    def back_fn():
        w.destroy()
        Menu_Page.menu_page_fun()

    i=Image.open("Empty.jpg").resize((1350,700))
    img=ImageTk.PhotoImage(i)
    my_lb=Label(image=img)
    my_lb.place(x=-2,y=-2)

    def clear_fun():
        us_ent.delete(0,END)
        em_ent.delete(0,END)
        po_ent.delete(0,END)
        cn_ent.delete(0,END)
        ex_ent.delete(0,END)
        cv_ent.delete(0,END)
        ps_ent.delete(0,END)
        r.unselect()

    #Log in
    hd_lb=Label(w,text="Login Page",font=("times",24,"bold"),fg="#FDFEFE",bg="#FFA500")
    hd_lb.place(x=600,y=1)

    #Username
    us_lb=Label(w,text="Username",font=("times",22,"bold"),bg="white",fg="#000000")
    us_lb.place(x=250,y=120)
    us_ent=Entry(w,font=("times",18),width=25,fg="#000000",selectbackground="blue",selectforeground="white")
    us_ent.place(x=600,y=120)

    #Email id
    em_lb=Label(w,text="Email id",font=("times",22,"bold"),bg="white",fg="#000000")
    em_lb.place(x=250,y=180)
    em_ent=Entry(w,font=("times",18),width=25,fg="#000000",selectbackground="blue",selectforeground="white")
    em_ent.place(x=600,y=180)

    #Phone no..
    po_lb=Label(w,text="Phone no..",font=("times",22,"bold"),bg="white",fg="#000000")
    po_lb.place(x=250,y=240)
    po_ent=Entry(w,font=("times",18),width=25,fg="#000000",selectbackground="blue",selectforeground="white")
    po_ent.place(x=600,y=240)

    #Card Number
    cn_lb=Label(w,text="Credit/Debit Card no..",font=("times",22,"bold"),bg="white",fg="#000000")
    cn_lb.place(x=250,y=300)
    cn_ent=Entry(w,font=("times",18),width=25,fg="#000000",selectbackground="blue",selectforeground="white")
    cn_ent.place(x=600,y=300)

    #Expiration date
    ex_lb=Label(w,text="Expiration date",font=("times",22,"bold"),bg="white",fg="#000000")
    ex_lb.place(x=250,y=360)
    ex_ent=Entry(w,font=("times",18),width=25,fg="#000000",selectbackground="blue",selectforeground="white")
    ex_ent.place(x=600,y=360)

    #CVV/CVC code
    cv_lb=Label(w,text="CVV/CVC code",font=("times",22,"bold"),bg="white",fg="#000000")
    cv_lb.place(x=250,y=420)
    cv_ent=Entry(w,font=("times",18),width=25,fg="#000000",selectbackground="blue",selectforeground="white")
    cv_ent.place(x=600,y=420)

    #Password
    ps_lb=Label(w,text="Password",font=("times",22,"bold"),bg="white",fg="#000000")
    ps_lb.place(x=250,y=480)
    ps_ent=Entry(w,font=("times",18),width=25,fg="#000000",selectbackground="blue",selectforeground="white")
    ps_ent.place(x=600,y=480)

    r=IntVar()

    rd1=Radiobutton(w,text="You are solely responsible for managing and maintaining the security of any information relating to such credentials and agree that Bitcoin.com shall not be held responsible",font=("times",12),fg="#000000",bg="white",value=1,variable=r)
    rd1.place(x=180,y=530)

    lb=Label(w,text="(and you shall not hold us responsible) for any unauthorised access to the Services or any resulting harm you may suffer.",font=("times",12),fg="#000000",bg="white")
    lb.place(x=200,y=555)

    #Next
    lg_lb=Button(w,text="Next",font=("times",15),bg="#1D8348",fg="#FBFCFC",bd=2,width=10,activebackground="#F4ECF7",activeforeground="#000000",command=buy_fun)
    lg_lb.place(x=500,y=600)

    #Clear
    clr_lb=Button(w,text="Clear",font=("times",15),bg="#F4D03F",fg="#000000",bd=2,width=10,activebackground="#F4ECF7",activeforeground="#17202A",command=clear_fun)
    clr_lb.place(x=730,y=600)

    click_here=Button(w,text="back",font=("times",15,"bold"),bg="orange",fg="white",activebackground="#EB984E",width=8,height=1,border=0,command=back_fn)
    click_here.place(x=50,y=600)

    w.mainloop()