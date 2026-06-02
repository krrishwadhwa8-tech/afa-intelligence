import yfinance as yf

print("Fetching RELIANCE data...")

ticker = yf.Ticker("RELIANCE.NS")

data = ticker.history(period="5d")

print(data)