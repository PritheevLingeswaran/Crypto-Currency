from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import requests
import Menu_Page
def tr():
    class CryptoTracker:
        def __init__(self,w):
            self.w =w
            # Create a label
            self.label =Label(w,text="Select any Cryptocurrency to view their Price",font=("times",22,),fg="#000000",bg="white")
            self.label.place(x=40,y=100)

            # Create a Combobox
            self.crypto_combobox = ttk.Combobox(w,font=("times",16),width=19,values=self.get_crypto_list())
            self.crypto_combobox.place(x=40,y=150)
            self.crypto_combobox.current(0)  
            # Set default selection

            # Create a button to check price
            self.check_price_button =Button(w,text="Check Price",font=("times",15),bg="orange",fg="white",activebackground="#ffa500",activeforeground="white",border=1,command=self.check_price)
            self.check_price_button.place(x=40,y=300)

            # Create a label to display the price
            self.price_label =Label(w,font=("times",15),text="",background="white")
            self.price_label.place(x=40,y=380)

        def get_crypto_list(self):
            # List of cryptocurrencies to track
            return ['Bitcoin', 'Ethereum', 'Ripple', 'Litecoin', 'Cardano', 
                        'Polkadot', 'Chainlink', 'Bitcoin Cash', 'Stellar', 
                        'Dogecoin', 'Uniswap', 'Terra', 'Avalanche', 'Solana', 
                        'Polygon', 'Cosmos', 'VeChain', 'Algorand', 'Filecoin', 
                        'Aave']

        def check_price(self):
            crypto_name = self.crypto_combobox.get()
            price = self.get_crypto_price(crypto_name)
            if price is not None:
                self.price_label.config(text="The Prize of "f"{crypto_name} Coin is ${price:.2f}")
            else:
                self.price_label.config(text="Error fetching price.")

        def get_crypto_price(self, crypto_name):
            # API endpoint for CoinGecko
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_name.lower()}&vs_currencies=usd"
            try:
                response = requests.get(url)
                data = response.json()
                return data[crypto_name.lower()]['usd']
            except Exception as e:
                print(f"Error: {e}")
                return None
    # if __name__ == "__main__":

    w=Tk()
    w.geometry("1350x690")
    w.configure(bg="White")

    def back_fn():
        w.destroy()
        Menu_Page.menu_page_fun()

    i=Image.open("Types.jpg").resize((1350,690))
    img=ImageTk.PhotoImage(i)

    my_lb=Label(image=img)
    my_lb.place(x=-2,y=-2)

    #CryptoCurrency Tracker
    hd_lb=Label(w,text="Cryptocurrency Tracker",font=("times",26,"bold"),fg="#FDFEFE",bg="#FFA500")
    hd_lb.place(x=500,y=7)

    click_here=Button(w,text="back",font=("times",15,"bold"),bg="orange",fg="white",activebackground="#EB984E",width=8,height=1,border=0,command=back_fn)
    click_here.place(x=50,y=600)

    app = CryptoTracker(w)
    w.mainloop()
