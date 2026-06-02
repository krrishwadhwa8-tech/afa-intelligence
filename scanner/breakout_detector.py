import yfinance as yf

symbol = "RELIANCE.NS"

df = yf.download(
    symbol,
    period="60d",
    progress=False,
    auto_adjust=False
)

close_price = df["Close"].iloc[-1].iloc[0]

previous_high = (
    df["High"]
    .iloc[-21:-1]
    .max()
    .iloc[0]
)

print(f"\n{symbol}")
print(f"Current Close : {close_price:.2f}")
print(f"20-Day High   : {previous_high:.2f}")

if close_price > previous_high:
    print("\n🚀 BREAKOUT DETECTED")
else:
    print("\nNo breakout.")