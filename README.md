💰 Crypto Currency Predictor & Trading Simulator

A Python-based cryptocurrency project that allows users to buy and sell cryptocurrencies in a simulated environment and predicts the future prices of major digital assets using machine learning.

🚀 Features

🪙 Buy & Sell Cryptocurrencies – Simulate real trading with virtual money.

📈 Live Price Tracking – Fetches the latest cryptocurrency prices from APIs.

🤖 Price Prediction – Uses a trained ML model to forecast future prices of Bitcoin, Ethereum, and other coins.

📊 Portfolio Management – Displays your wallet balance and owned coins in real time.

🔍 Historical Data Visualization – Interactive charts to view past trends.

⚙️ Modular Design – Cleanly separated modules for API handling, trading logic, and prediction models.

🧠 Tech Stack
Component	Technology Used
Language	Python
Libraries	pandas, numpy, scikit-learn, matplotlib, requests
Data Source	CoinGecko / Binance API
Prediction Model	Linear Regression / LSTM (based on your implementation)
Storage	Local JSON / SQLite database for transaction logs
🧩 Project Structure
CryptoPredictor/
│
├── data/                  # Historical crypto data
├── models/                # Saved ML models
├── utils/                 # Helper functions (API, plotting, etc.)
├── main.py                # Main entry point
├── trading.py             # Buy/Sell and portfolio logic
├── prediction.py          # Model training and prediction
├── requirements.txt       # Required Python libraries
└── README.md              # Project documentation

⚙️ Installation & Setup



Install Dependencies

pip install -r requirements.txt


Run the Application

python main.py


(Optional) Update your API key in the config file if you’re using Binance API.

🔮 How It Works

The app fetches real-time cryptocurrency data using the CoinGecko/Binance API.

The machine learning model (Linear Regression or LSTM) is trained on past price data.

The system predicts future prices and displays them alongside real-time prices.

Users can buy or sell coins using virtual money, and their portfolio updates dynamically.

🧾 Example Output
Welcome to CryptoPredictor 💰
---------------------------------
Available Balance: $10,000
1. Buy Crypto
2. Sell Crypto
3. View Portfolio
4. Predict Prices
5. Exit
Enter your choice: 4

🔮 Predicted BTC Price for Tomorrow: $67,420

🧑‍💻 Future Improvements

Add deep learning-based LSTM model for more accurate predictions

Integrate real trading APIs (Binance testnet)

Add user authentication system

Create a web dashboard using Flask or Streamlit

📜 License

This project is licensed under the MIT License – free to use and modify.

🌟 Author

Developed by Pritheev Kumar

🎯 Final Year CSE Student | 💡 Aspiring AI/ML Developer | 📍 SRM University, Chennai




Developed by Pritheev Kumar

🎯 Final Year CSE Student | 💡 Aspiring AI/ML Developer | 📍 SRM University, Chennai
