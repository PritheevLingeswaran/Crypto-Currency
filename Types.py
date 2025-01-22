from tkinter import*
from PIL import Image,ImageTk
import Menu_Page
def types_fn():

    w=Tk()
    w.title("Real Time Project")
    w.geometry("1350x690")

    def back_fn():
        w.destroy()
        Menu_Page.menu_page_fun()

    i=Image.open("Types.jpg").resize((1350,700))
    img=ImageTk.PhotoImage(i)
    my_lb=Label(image=img)
    my_lb.place(x=-2,y=-2)

    #Types of Crypto Currencies
    hd_lb=Label(w,text="Types of Crypto Currencies",font=("times",28,"bold"),fg="#FDFEFE",bg="#FFA500")
    hd_lb.place(x=475,y=7)

    #Currencies
    type_lb=Label(w,text="1. Bitcoin (BTC)",font=("times",22),fg="#000000",bg="white")
    type_lb.place(x=40,y=80)
    type_lb=Label(w,text="2. Ether (ETH)",font=("times",22),fg="#000000",bg="white")
    type_lb.place(x=40,y=130)
    type_lb=Label(w,text="3. Binance Coin (BNB)",font=("times",22),fg="#000000",bg="white")
    type_lb.place(x=40,y=180)
    type_lb=Label(w,text="4. Tether (USDT)",font=("times",22),fg="#000000",bg="white")
    type_lb.place(x=40,y=230)
    type_lb=Label(w,text="5. Solana (SOL)",font=("times",22),fg="#000000",bg="white")
    type_lb.place(x=40,y=280)
    type_lb=Label(w,text="6. XRP (XRP)",font=("times",22),fg="#000000",bg="white")
    type_lb.place(x=40,y=330)
    type_lb=Label(w,text="7. Cardano (ADA)",font=("times",22),fg="#000000",bg="white")
    type_lb.place(x=40,y=380)
    type_lb=Label(w,text="8. USD Coin (USDC)",font=("times",22),fg="#000000",bg="white")
    type_lb.place(x=40,y=430)
    type_lb=Label(w,text="9. Aave (AAVE)",font=("times",22),fg="#000000",bg="white")
    type_lb.place(x=40,y=480)
    type_lb=Label(w,text="10. Avalanche (AVAX)",font=("times",22),fg="#000000",bg="white")
    type_lb.place(x=40,y=530)

    click_here=Button(w,text="back",font=("times",15,"bold"),bg="orange",fg="white",activebackground="#EB984E",width=8,height=1,border=0,command=back_fn)
    click_here.place(x=1200,y=620)

    w.mainloop()