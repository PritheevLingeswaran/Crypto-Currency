from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import Details
def buy_fn():

    # Sample list of cryptocurrencies
    cryptocurrencies = [
        "Bitcoin", "Ethereum", "Ripple", "Litecoin", "Cardano",
        "Polkadot", "Chainlink", "Bitcoin Cash", "Stellar", "Dogecoin",
        "Uniswap", "Solana", "Avalanche", "Polygon", "VeChain",
        "Tezos", "Cosmos", "Algorand", "Filecoin", "Aave"
    ]

    class CryptoWalletApp:
        def __init__(self, w):
            self.w = w
            self.w.title("Crypto Wallet")

            # Initialize wallet
            self.wallet = {}

            # Create UI components
            self.create_widgets()

        def create_widgets(self):
            # ComboBox for selecting cryptocurrency
            self.crypto_label =Label(self.w,text="Select Cryptocurrency:",font=("times",22),fg="#000000",bg="white")
            self.crypto_label.place(x=150,y=100)

            self.crypto_combo = ttk.Combobox(self.w,font=("times",16),width=19,values=cryptocurrencies)
            self.crypto_combo.place(x=150,y=160)

            # Entry for amount
            self.amount_label =Label(self.w,text="Enter Amount in USD:",font=("times",22),fg="#000000",bg="white")
            self.amount_label.place(x=150,y=260)

            self.amount_entry =Entry(self.w,font=("times",16),width=19)
            self.amount_entry.place(x=150,y=320)

            # Buttons for buy and sell
            self.buy_button =Button(self.w, text="Buy",font=("times",15),bg="Green",fg="white",border=1,command=self.buy_crypto)
            self.buy_button.place(x=150,y=380)

            self.sell_button =Button(self.w, text="Sell", font=("times",15),bg="Red",fg="white",border=1,command=self.sell_crypto)
            self.sell_button.place(x=300,y=380)
                            
            # Display wallet
            self.wallet_display =Text(self.w, width=30, height=10,font=("times",20))
            self.wallet_display.place(x=700,y=150)

            self.update_wallet_display()

        def buy_crypto(self):
            crypto = self.crypto_combo.get()
            amount = self.amount_entry.get()

            if not crypto or not amount:
                messagebox.showerror("Input Error", "Please select a cryptocurrency and enter an amount.")
                return

            try:
                amount = float(amount)
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid amount.")
                return

            if crypto in self.wallet:
                self.wallet[crypto] += amount
            else:
                self.wallet[crypto] = amount

            messagebox.showinfo("Success", f"Bought {amount} USD of {crypto}!")
            self.update_wallet_display()

        def sell_crypto(self):
            crypto = self.crypto_combo.get()
            amount = self.amount_entry.get()

            if not crypto or not amount:
                messagebox.showerror("Input Error", "Please select a cryptocurrency and enter an amount.")
                return

            try:
                amount = float(amount)
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid amount.")
                return

            if crypto in self.wallet and self.wallet[crypto] >= amount:
                self.wallet[crypto] -= amount
                messagebox.showinfo("Success", f"Sold {amount} USD of {crypto}!")
                if self.wallet[crypto] == 0:
                    del self.wallet[crypto]
            else:
                messagebox.showerror("Sell Error", "Insufficient funds to sell.")

            self.update_wallet_display()

        def update_wallet_display(self):
            self.wallet_display.delete(1.0,END)  # Clear the text area
            for crypto, amount in self.wallet.items():
                self.wallet_display.insert(END, f"{crypto}: ${amount:.2f}\n")

    
    w=Tk()
    w.geometry("1350x690")

    def back_fn():
        w.destroy()
        Details.details_fn()

    i=Image.open("Empty.jpg").resize((1350,690))
    img=ImageTk.PhotoImage(i)

    my_lb=Label(image=img)
    my_lb.place(x=-2,y=-2)

    #Buy and Sell Cryptocurrencies
    hd_lb=Label(w,text="Buy and Sell Cryptocurrencies",font=("times",24,"bold"),fg="#FDFEFE",bg="#FFA500")
    hd_lb.place(x=490,y=1)

    #Your Wallet
    wa_lb=Label(w,text="Your Wallet:",font=("times",20),fg="#000000",bg="white")
    wa_lb.place(x=700,y=100)   
    app = CryptoWalletApp(w)

    click_here=Button(w,text="back",font=("times",15,"bold"),bg="orange",fg="white",activebackground="#EB984E",width=8,height=1,border=0,command=back_fn)
    click_here.place(x=50,y=630)

    w.mainloop()
